from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Order


@login_required
def order_list_view(request):
    # agar user freelancer bo‘lsa — freelancer_orders
    freelancer_orders = request.user.freelancer_orders.all()

    # agar user client bo‘lsa — client_orders
    client_orders = request.user.client_orders.all()

    return render(request, 'orders/order_list.html', {
        'freelancer_orders': freelancer_orders,
        'client_orders': client_orders
    })


@login_required
def order_detail_view(request, pk):
    # orderni topamiz
    order = get_object_or_404(Order, pk=pk)

    # faqat client yoki freelancer ko‘ra oladi
    if request.user not in [order.client, order.freelancer]:
        return HttpResponseForbidden("Bu order sizga tegishli emas")

    return render(request, 'orders/order_detail.html', {'order': order})


@login_required
def order_accept_view(request, pk):
    # freelancer orderni qabul qiladi
    order = get_object_or_404(Order, pk=pk)

    if request.user != order.freelancer:
        return HttpResponseForbidden("Faqat freelancer qabul qila oladi")

    if order.status == 'pending':
        order.status = 'active'
        order.save()

    return redirect('order_detail', pk=order.pk)


@login_required
def order_complete_view(request, pk):
    # freelancer ishni tugatadi
    order = get_object_or_404(Order, pk=pk)

    if request.user != order.freelancer:
        return HttpResponseForbidden("Faqat freelancer tugata oladi")

    if order.status == 'active':
        order.status = 'completed'
        order.save()

    return redirect('order_detail', pk=order.pk)


@login_required
def order_cancel_view(request, pk):
    # client bekor qiladi
    order = get_object_or_404(Order, pk=pk)

    if request.user != order.client:
        return HttpResponseForbidden("Faqat client bekor qila oladi")

    if order.status == 'pending':
        order.status = 'cancelled'
        order.save()

    return redirect('order_detail', pk=order.pk)
