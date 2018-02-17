from django.apps import AppConfig


class ProfilesAppConfig(AppConfig):
    name = 'apps.profiles'

    def ready(self):
        import apps.profiles.signals


default_app_config = 'apps.profiles.ProfilesAppConfig'
