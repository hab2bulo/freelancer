from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'apps.accounts'

    def ready(self):
        # signals.py ni Django yuklab olishi uchun
        import apps.accounts.signals