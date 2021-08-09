from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from ..models import Order
from django.db.models import Q
from .process_views import process_add

def watchlist(request):
    page = request.GET.get('page', '1')
    user_id = request.GET['user_id']

    # 조회
    order_list = Order.objects.order_by('order_date')
    order_list = order_list.filter(
        Q(watch_users=user_id)
    ).distinct()

    paginator = Paginator(order_list, 50)
    page_obj = paginator.get_page(page)

    page_obj = process_add(page_obj)

    context = {'order_list': page_obj, 'page': page}

    return render(request, 'opman/order_table.html', context)

@login_required(login_url='common:login')
def add_watch_user(request, _id_str):
    _id_arr = list(filter(None, _id_str[1:].split('$')))
    for order_id in _id_arr:
        order = Order.objects.get(pk=order_id)
        order.watch_users.add(request.user.id)

    return redirect('opman:index')

@login_required(login_url='common:login')
def del_watch_user(request, _id_str):
    _id_arr = list(filter(None, _id_str[1:].split('$')))
    for order_id in _id_arr:
        order = Order.objects.get(pk=order_id)
        order.watch_users.remove(request.user.id)

    return redirect('opman:index')
