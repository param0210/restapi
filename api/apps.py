from django.apps import AppConfig
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _


class ApiConfig(AppConfig):
    name = 'api'
    
    def ready(self):
        import api. signals

