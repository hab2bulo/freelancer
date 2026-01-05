from django.db import models
from django.contrib.auth.models import User
from apps.core.models import TimeStampedModel


class Wallet(TimeStampedModel):
    # qaysi userga tegishli
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    # balans
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)


class Transaction(TimeStampedModel):
    # qaysi wallet bilan bog‘liq
    wallet = models.ForeignKey(
        Wallet,
        on_delete=models.CASCADE
    )

    # tranzaksiya summasi
    amount = models.DecimalField(max_digits=12, decimal_places=2)

    # tranzaksiya turi (kirim/chiqim)
    transaction_type = models.CharField(max_length=20)
