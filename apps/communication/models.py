from django.db import models
from apps.core.models import TimeStampedModel
from apps.accounts.models import Profile
from apps.orders.models import Order


class Message(TimeStampedModel):
    # qaysi order bo‘yicha yozilyapti (chat orderga bog‘liq)
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='messages'
        
    )

    # kim yubordi
    sender = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

    # xabar matni
    text = models.TextField()
    # o'qilgan yoki yo'qligi
    is_read = models.BooleanField(default=False)
    def __str__(self):
        return f"Message from {self.sender.user.username} in Order #{self.order.id}"