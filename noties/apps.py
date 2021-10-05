from django.apps import AppConfig


class NotiesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'noties'

    def ready(self):
        import noties.signals

