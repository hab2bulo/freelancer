from django.db import models
from apps.core.models import TimeStampedModel
from apps.accounts.models import Profile
from apps.orders.models import Order


class Message(TimeStampedModel):
    # qaysi orderga tegishli chat
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='messages'
    )

    # kim yubordi (client yoki freelancer)
    sender = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='sent_messages'
    )

    # xabar matni
    text = models.TextField()

    # o‘qilgan yoki yo‘qligi
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message #{self.id} (Order {self.order.id})"
