from django.db import models
from django.contrib.auth.models import User
from apps.core.models import TimeStampedModel
from apps.orders.models import Order


class Review(TimeStampedModel):
    # qaysi buyurtma uchun
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )

    # review yozgan foydalanuvchi
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    # kimga yozilgan (client yoki freelancer)
    target = models.ForeignKey(
        User,
        related_name='reviews_received',
        on_delete=models.CASCADE
    )

    # baho (1–5)
    rating = models.PositiveSmallIntegerField()

    # izoh
    comment = models.TextField(blank=True)
    def __str__(self):
        return f"{self.author.username} → {self.target.username} ({self.rating}⭐)"