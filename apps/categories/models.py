from django.db import models
from apps.core.models import TimeStampedModel


class Category(TimeStampedModel):
    # kategoriya nomi (Design, IT, Marketing)
    name = models.CharField(max_length=120)

    # SEO va URL uchun slug
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Skill(TimeStampedModel):
    # skill nomi (Python, React, Photoshop)
    name = models.CharField(max_length=120)

    # qaysi kategoriyaga tegishli
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
