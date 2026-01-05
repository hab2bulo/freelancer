from django.db import models


class TimeStampedModel(models.Model):
    # obyekt qachon yaratilganini avtomatik saqlaydi
    created_at = models.DateTimeField(auto_now_add=True)

    # obyekt qachon oxirgi marta o‘zgartirilganini saqlaydi
    updated_at = models.DateTimeField(auto_now=True)

    # soft delete uchun (o‘chirmaymiz, faqat faol emas qilamiz)
    is_active = models.BooleanField(default=True)

    class Meta:
        # bu model alohida jadval bo‘lmaydi
        abstract = True
