from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Message
from .forms import MessageForm
from apps.orders.models import Order


@login_required
def order_chat_view(request, order_id):
    # orderni topamiz
    order = get_object_or_404(Order, id=order_id)

    # faqat client yoki freelancer chat qila oladi
    if request.user not in [order.client, order.freelancer]:
        return HttpResponseForbidden("Bu chat sizga tegishli emas")

    # orderga tegishli barcha xabarlar
    messages = order.messages.select_related('sender__user')

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)

            # xabar qaysi orderga tegishli
            message.order = order

            # xabar yuboruvchi (profile orqali)
            message.sender = request.user.profile

            message.save()
            return redirect('order_chat', order_id=order.id)
    else:
        form = MessageForm()

    return render(request, 'communication/chat.html', {
        'order': order,
        'messages': messages,
        'form': form
    })
