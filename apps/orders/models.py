# Django ORM asosiy moduli
from django.db import models

# Custom user bo‘lsa ham ishlashi uchun
from django.conf import settings

# Model validation uchun
from django.core.exceptions import ValidationError

# created_at va updated_at qo‘shib beradigan base model
from apps.core.models import TimeStampedModel

# Service orqali order berish uchun
from apps.services.models import Service

# Proposal orqali order berish uchun (project bidding)
from apps.projects.models import Proposal


class Order(TimeStampedModel):
    """
    ORDER MODELI

    Order faqat:
    - service OR
    - proposal

    asosida yaratiladi (ikkalasi bir vaqtda bo‘lishi mumkin emas).
    """

    # ---------- BUYURTMA HOLATLARI ----------

    # Client order berdi, freelancer hali qabul qilmagan
    STATUS_PENDING = 'pending'

    # Freelancer orderni qabul qildi
    STATUS_ACCEPTED = 'accepted'

    # Ish jarayoni boshlandi
    STATUS_IN_PROGRESS = 'in_progress'

    # Ish tugatildi va topshirildi
    STATUS_COMPLETED = 'completed'

    # Order bekor qilindi
    STATUS_CANCELLED = 'cancelled'

    # Status tanlovlari (admin va form uchun)
    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_ACCEPTED, 'Accepted'),
        (STATUS_IN_PROGRESS, 'In progress'),
        (STATUS_COMPLETED, 'Completed'),
        (STATUS_CANCELLED, 'Cancelled'),
    ]

    # ---------- ORDER MANBASI ----------

    # Agar order tayyor service orqali berilgan bo‘lsa
    service = models.ForeignKey(
        Service,                      # qaysi service
        null=True,                    # proposal bo‘lsa, bo‘sh qoladi
        blank=True,
        on_delete=models.SET_NULL     # service o‘chsa order saqlanib qoladi
    )

    # Agar order project/proposal orqali berilgan bo‘lsa
    proposal = models.ForeignKey(
        Proposal,                     # qaysi proposal
        null=True,                    # service bo‘lsa, bo‘sh qoladi
        blank=True,
        on_delete=models.SET_NULL     # proposal o‘chsa order saqlanib qoladi
    )

    # ---------- BUYURTMA ISHTIROKCHILARI ----------

    # BUYURTMANI BERGAN MIJOZ (CLIENT)
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,     # Django User modeli
        related_name='orders_as_client',  # client.orders_as_client.all()
        on_delete=models.CASCADE      # client o‘chsa order ham o‘chadi
    )

    # BUYURTMANI BAJARADIGAN FREELANCER
    freelancer = models.ForeignKey(
        settings.AUTH_USER_MODEL,         # freelancer ham User
        related_name='orders_as_freelancer',  # freelancer.orders_as_freelancer.all()
        on_delete=models.CASCADE
    )

    # ---------- ORDER MA'LUMOTLARI ----------

    # BUYURTMA PAYTIDAGI NARX (SNAPSHOT)
    # Service yoki proposal keyin o‘zgarsa ham bu qiymat o‘zgarmaydi
    price = models.DecimalField(
        max_digits=10,                # maksimal 10 xonali son
        decimal_places=2              # 2 xonali kasr (pul uchun ideal)
    )

    # BUYURTMA YAKUNIY MUDDATI
    deadline = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Buyurtma topshirilishi kerak bo‘lgan oxirgi vaqt"
    )

    # BUYURTMA HOLATI
    status = models.CharField(
        max_length=20,                # status string uzunligi
        choices=STATUS_CHOICES,       # faqat belgilangan holatlar mumkin
        default=STATUS_PENDING        # default holat
    )

    # ---------- LOGIKA VA HIMOYA ----------

    def clean(self):
        """
        MODEL VALIDATION

        Order:
        - service YOKI proposal asosida bo‘lishi shart
        - ikkalasi bir vaqtda bo‘lishi mumkin emas
        """
        if not self.service and not self.proposal:
            raise ValidationError(
                "Order service yoki proposal asosida yaratilishi shart."
            )

        if self.service and self.proposal:
            raise ValidationError(
                "Order faqat bittasi orqali yaratiladi: service YOKI proposal."
            )

    def __str__(self):
        # Admin panel va shell uchun o‘qilishi qulay format
        return f"Order #{self.id} - {self.status}"
