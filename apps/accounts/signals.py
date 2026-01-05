from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    # agar yangi user yaratilgan bo‘lsa
    if created:
        # unga avtomatik Profile yaratamiz
        Profile.objects.create(
            user=instance,
            role='client'  # default rol (keyin o‘zgartiriladi)
        )
