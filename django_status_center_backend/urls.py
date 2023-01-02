from django.urls import path

from . import views

urlpatterns = [
    path("", views.export_all),
    path("<int:cat_id>/", views.export_category)
]
