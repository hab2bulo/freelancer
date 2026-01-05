from django.db import models
from django.contrib.auth.models import User
from apps.core.models import TimeStampedModel
from apps.services.models import Service
from apps.projects.models import Proposal


class Order(TimeStampedModel):
    # buyurtma holatlari
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    # agar service orqali buyurtma bo‘lsa
    service = models.ForeignKey(
        Service,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    # agar proposal orqali buyurtma bo‘lsa
    proposal = models.ForeignKey(
        Proposal,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    # buyurtmani bergan client
    client = models.ForeignKey(
        User,
        related_name='client_orders',
        on_delete=models.CASCADE
    )

    # ishni bajarayotgan freelancer
    freelancer = models.ForeignKey(
        User,
        related_name='freelancer_orders',
        on_delete=models.CASCADE
    )

    # buyurtma holati
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    # yakuniy narx
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    deadline = models.DateTimeField(
    null=True,
    blank=True,
    help_text="Buyurtma topshirilishi kerak bo‘lgan oxirgi vaqt"
)
    def __str__(self):
        return f'Order #{self.id} - {self.status}'