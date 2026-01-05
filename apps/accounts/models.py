from django.db import models
from django.contrib.auth.models import User
from apps.core.models import TimeStampedModel


class Profile(TimeStampedModel):
    # foydalanuvchi roli variantlari
    ROLE_CHOICES = (
        ('freelancer', 'Freelancer'),
        ('client', 'Client'),
        ('both', 'Both'),
    )

    # Django default User bilan 1 ta profil bog‘lanadi
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE  # user o‘chsa, profil ham o‘chadi
    )

    # foydalanuvchi qaysi rolda ishlaydi
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    # foydalanuvchi haqida qisqacha bio
    bio = models.TextField(blank=True)

    # profil rasmi (media/avatars/)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    # o‘rtacha reyting (reviewlardan hisoblanadi)
    rating = models.FloatField(default=0)

    # jami nechta review olgan
    total_reviews = models.PositiveIntegerField(default=0)

    # nechta buyurtma muvaffaqiyatli tugagan
    completed_orders = models.PositiveIntegerField(default=0)

    def __str__(self):
        # admin panelda username ko‘rinadi
        return self.user.username
