from django.apps import AppConfig


class MagazonAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'magazon_app'

    def ready(self):
        import magazon_app.signals
