from django.db import models
from apps.core.models import TimeStampedModel
from apps.accounts.models import Profile
from apps.categories.models import Category, Skill


class Service(TimeStampedModel):
    # xizmat egasi (freelancer)
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='services'
    )

    title = models.CharField(max_length=200)
    description = models.TextField()

    price = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_days = models.PositiveIntegerField()

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    
    skills = models.ManyToManyField(Skill, blank=True)

    views_count = models.PositiveIntegerField(default=0)
    orders_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    