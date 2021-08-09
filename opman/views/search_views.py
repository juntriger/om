from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from ..models import Order
from django.db.models import Q
from .process_views import process_add

def search_order(request):
    sql = Q(state='') | Q(state=1)

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
    order_list = Order.objects.order_by('-order_date')
    order_list = order_list.filter(sql).distinct()

    #paginator = Paginator(order_list, 50)
    #page_obj = paginator.get_page(page)

    page_obj = process_add(order_list)

    context['order_list'] = page_obj

    return render(request, 'opman/order_table.html', context)

def excel_paste(request):
    return render(request, 'opman/excel_paste.html')

def search_order_by_str(request):
    sql = Q(state='') | Q(state=1)

    page = request.GET.get('page', '1')
    order_arr = request.GET['order_arr']
    order_list = order_arr.split('&')

    sql = sql & Q(order_id=order_list[0].split('-')[0]) & Q(seq_num=order_list[0].split('-')[1])

    for order in order_list:
        sql = sql | Q(order_id=order.split('-')[0]) & Q(seq_num=order.split('-')[1])

    context = {'page': page}

    # 조회
    order_list = Order.objects.order_by('-order_date')
    order_list = order_list.filter(sql).distinct()

    order_list = process_add(order_list)

    context['order_list'] = order_list

    return render(request, 'opman/order_table.html', context)
