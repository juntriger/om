from django.core.paginator import Paginator
from django.shortcuts import render
from ..models import Order, Customer

def index(request):
    """
    오더 목록 출력
    """
    # 입력 인자
    page = request.GET.get('page', '1')

    # 조회
    order_list = Order.objects.order_by('-order_date')
    customer_list = Customer.objects.order_by('customer')

    # 페이지 처리
    paginator = Paginator(order_list, 50)
    page_obj = paginator.get_page(page)

    context = {'order_list': page_obj, 'customer_list': customer_list, 'page': page}

    return render(request, 'opman/order_process.html', context)

def order_process(request):
    """
    오더 목록 출력
    """
    # 입력 인자
    page = request.GET.get('page', '1')

    # 조회
    order_list = Order.objects.order_by('-order_date')

    # 페이지 처리
    paginator = Paginator(order_list, 50)
    page_obj = paginator.get_page(page)

    context = {'order_list': page_obj, 'page': page}

    return render(request, 'opman/order_table.html', context)