from django.apps import AppConfig


class BooksAppConfig(AppConfig):
    name = 'apps.products'

    def ready(self):
        import apps.products.signals


default_app_config = 'apps.products.BooksAppConfig'
