from django.urls import path
from . import views

urlpatterns = [
    path("tour/", views.tour_form, name="tour_form"),
    path("tour/export/", views.export_tours, name="export_tours"),
]