from django.contrib import admin

from django.apps import apps

from .models import *


for model in apps.get_app_config("django_status_center_model").models.values():
    admin.site.register(model)
