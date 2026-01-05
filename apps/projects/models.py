from django.db import models
from apps.core.models import TimeStampedModel   # created_at, updated_at avtomatik
from apps.accounts.models import Profile        # user + role (client/freelancer)
from apps.categories.models import Category     # loyiha kategoriyasi


class Project(TimeStampedModel):
    """
    Project — client tomonidan joylanadigan ish e’loni.
    Freelancerlar shu projectga proposal yuboradi.
    """

    # Project egasi (faqat client yoki both bo‘lishi kerak)
    # Profile ishlatiladi — keyinchalik order, review, chat uchun muhim
    client = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='projects'
    )

    # Loyiha sarlavhasi (list va search uchun)
    title = models.CharField(max_length=200)

    # Loyiha tavsifi (freelancer shu asosida proposal yozadi)
    description = models.TextField()

    # Client taklif qilayotgan maksimal byudjet
    # Order summasi shu qiymatdan olinadi
    budget = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    # Loyiha qaysi kategoriya ichida
    # Category o‘chsa ham project saqlanib qoladi
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True
    )

    # Loyiha ochiqmi yoki yopilganmi
    # Proposal qabul qilinayotgan bo‘lsa True
    # Freelancer tanlangach False qilinadi
    is_open = models.BooleanField(default=True)

    def __str__(self):
        # Admin panel va debug uchun qulay ko‘rinish
        return self.title


class Proposal(TimeStampedModel):
    """
    Proposal — freelancer tomonidan projectga yuborilgan taklif.
    """

    # Qaysi projectga proposal berilgan
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='proposals'
    )

    # Qaysi freelancer proposal berdi
    # Profile ishlatiladi — role va review uchun muhim
    freelancer = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='proposals'
    )

    # Freelancerning xabari (tajriba, reja, yondashuv va h.k.)
    message = models.TextField()

    # Freelancer taklif qilayotgan narx
    # Order yaratilganda shu summa olinadi
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    # Proposal holati:
    # pending  — client hali qaror qilmagan
    # accepted — proposal qabul qilindi → order yaratiladi
    # rejected — proposal rad etildi
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending'
    )

    class Meta:
        # Bitta freelancer bitta projectga faqat 1 marta proposal bera oladi
        unique_together = ('project', 'freelancer')

    def __str__(self):
        # Admin panel va debug uchun
        return f"{self.freelancer.user.username} → {self.project.title}"
