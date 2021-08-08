from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Order, Customer, User
from django.db.models import Q

def index(request):
    """
    오더 목록 출력
    """
    # 입력 인자
    page = request.GET.get('page', '1')

    # 조회
    order_list = Order.objects.order_by('order_date')
    customer_list = Customer.objects.order_by('customer')

    # 페이지 처리
    paginator = Paginator(order_list, 50)
    page_obj = paginator.get_page(page)

    context = {'order_list': page_obj, 'customer_list': customer_list, 'page': page}

    return render(request, 'opman/order_process.html', context)

def order_list(request):
    """
    오더 목록 출력
    """
    # 입력 인자
    page = request.GET.get('page', '1')

    # 조회
    order_list = Order.objects.order_by('order_date')

    # 페이지 처리
    paginator = Paginator(order_list, 50)
    page_obj = paginator.get_page(page)

    context = {'order_list': page_obj, 'page': page}

    return render(request, 'opman/order_table.html', context)

def search_order(request):

    page = request.GET.get('page', '1')

    order_id_kw = request.GET['order_id_kw']
    seq_num_kw = request.GET['seq_num_kw']
    po_code_kw = request.GET['po_code_kw']
    customer_kw = request.GET['customer_kw']
    item_kw = request.GET['item_kw']
    color_code_kw = request.GET['color_code_kw']
    pattern_kw = request.GET['pattern_kw']
    order_qty_kw = request.GET['order_qty_kw']

    context = {'page': page}

    sql = Q(state='') | Q(state=1)

    # 입력 인자 전달
    if order_id_kw:
        context['order_id'] = order_id_kw
        sql = sql & Q(order_id__icontains=order_id_kw)

    if seq_num_kw != '':
        context['seq_num'] = seq_num_kw
        sql = sql & Q(seq_num=seq_num_kw)

    if po_code_kw != '':
        context['customer_po'] = po_code_kw
        sql = sql & Q(customer_po__icontains=po_code_kw)

    if customer_kw != 'Any':
        context['customer'] = customer_kw
        sql = sql & Q(customer=customer_kw)

    if item_kw != '':
        context['item'] = item_kw
        sql = sql & Q(item__icontains=item_kw)

    if color_code_kw != '':
        context['color_code'] = color_code_kw
        sql = sql & Q(color_code__icontains=color_code_kw)

    if pattern_kw != '':
        context['pattern'] = pattern_kw
        sql = sql & Q(pattern__icontains=pattern_kw)

    if order_qty_kw != '':
        context['order_qty'] = order_qty_kw
        sql = sql & Q(order_qty=order_qty_kw)

    # 조회
    order_list = Order.objects.order_by('order_date')
    order_list = order_list.filter(sql).distinct()
    customer_list = Customer.objects.order_by('customer')

    paginator = Paginator(order_list, 50)
    page_obj = paginator.get_page(page)

    context['order_list'] = page_obj
    context['customer_list']: customer_list

    return render(request, 'opman/order_table.html', context)


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

def excel_paste(request):
    return render(request, 'opman/excel_paste.html')


"""
# 오더 삭제
@login_required(login_url='common:login')
def del_order(request, _id_str):
    _id_arr = list(filter(None, _id_str[1:].split('$')))
    for order_id in _id_arr:
        watchlist = get_object_or_404(Order, pk=order_id)
        print(watchlist)
        watchlist.delete()

    return redirect('opman:index')
"""


# Create your views here.
