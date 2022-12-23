from django.apps import AppConfig


class HarvestsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'harvests'

    def ready(self):
        import harvests.signals
