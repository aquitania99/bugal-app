"""Core App"""

# Django
from django.apps import AppConfig


class BaseAppConfig(AppConfig):
    """Base app config"""

    name = 'bugal.base'  # Module name - Bugal Core - Common classes module
    verbose_name = 'Base'  # How the module will be invoked
