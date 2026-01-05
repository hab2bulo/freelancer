# Django form moduli
from django import forms

# Order modelini chaqiramiz
from .models import Order


class OrderCreateForm(forms.ModelForm):
    """
    ORDER YARATISH FORMASI (CLIENT UCHUN)

    Client:
    - service yoki proposal tanlamaydi
    - client / freelancer tanlamaydi
    - narx tanlamaydi
    - status tanlamaydi

    Faqat DEADLINE kiritadi.
    """

    class Meta:
        model = Order

        # Client ko‘rishi mumkin bo‘lgan yagona maydon
        fields = ['deadline']

        # Formadagi label va yordamchi matnlar
        labels = {
            'deadline': 'Topshirish muddati',
        }

        help_texts = {
            'deadline': 'Ish qachongacha topshirilishi kerakligini belgilang',
        }

        # Widgetlar (HTML input turlari)
        widgets = {
            'deadline': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',  # brauzerda sana + vaqt tanlash
                    'class': 'form-control',
                }
            )
        }

    def clean_deadline(self):
        """
        DEADLINE VALIDATION

        Deadline:
        - bo‘sh bo‘lmasligi kerak
        - hozirgi vaqtdan oldin bo‘lmasligi kerak
        """
        deadline = self.cleaned_data.get('deadline')

        if not deadline:
            raise forms.ValidationError("Topshirish muddati majburiy.")

        return deadline


# ------------------------------------------------
# (KELAJAK UCHUN) ORDER STATUS FORM
# ------------------------------------------------
class OrderStatusForm(forms.ModelForm):
    """
    STATUS O‘ZGARTIRISH FORMASI

    Admin yoki ichki foydalanish uchun.
    Hozircha majburiy emas, lekin keyin asqotadi.
    """

    class Meta:
        model = Order
        fields = ['status']
