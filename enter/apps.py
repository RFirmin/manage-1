from django.apps import AppConfig


class EnterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'enter'

    def ready(self):
        import enter.signals
