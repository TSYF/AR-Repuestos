from django.urls import path
from .views import detailing_store, detailing_index

urlpatterns = [
    path("contacto-detailing", detailing_index, name="detailing.index"),
    path("contacto-detailing/store", detailing_store, name="detailing.store")
]
