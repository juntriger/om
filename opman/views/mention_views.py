from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone
from ..forms import MentionForm
from ..models import Order, Process, Mention

@login_required(login_url='common:login')
def mention_view(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    prcs_list = Process.objects.filter(order=order)
    context = {'order': order, 'prcs_list':prcs_list}

    return render(request, 'opman/order_mention.html', context)

@login_required(login_url='common:login')
def mention_create(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        form = MentionForm(request.POST)
        if form.is_valid():
            mention = form.save(commit=False)
            mention.author = request.user  # 추가한 속성 author 적용
            mention.create_date = timezone.now()
            mention.question = order
            mention.save()
            return redirect('{}#mention_{}'.format(
                resolve_url('opman:mention_view', order_id=order.id), mention.id))
    else:
        form = MentionForm()
    context = {'question': order, 'form': form}
    return render(request, 'opman/order_mention.html', context)


@login_required(login_url='common:login')
def mention_modify(request, mention_id):
    mention = get_object_or_404(Mention, pk=mention_id)
    if request.user != mention.author:
        messages.error(request, '수정 권한이 없습니다')
        return redirect('opman:mention_view', order_id=mention.order.id)

    if request.method == "POST":
        form = MentionForm(request.POST, instance=mention)
        if form.is_valid():
            mention = form.save(commit=False)
            mention.author = request.user
            mention.modify_date = timezone.now()
            mention.save()
            return redirect('{}#mention_{}'.format(
                resolve_url('opman:mention_view', order_id=mention.order.id), mention.id))
    else:
        form = MentionForm(instance=mention)
    context = {'answer': mention, 'form': form}

    return render(request, 'opman/mention_form.html', context)


@login_required(login_url='common:login')
def mention_delete(request, mention_id):
    mention = get_object_or_404(Mention, pk=mention_id)
    if request.user != mention.author:
        messages.error(request, '삭제 권한이 없습니다')
    else:
        mention.delete()
    return redirect('opman:mention_view', order_id=mention.order.id)
