from django.apps import AppConfig

class CetaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ceta'

    def ready(self): 
        import ceta.signals
