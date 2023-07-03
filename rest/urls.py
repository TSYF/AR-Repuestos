from django.urls import path
from .views import detailing_store, detailing_index, carro_index, carro_store, carro_delete, carro_update

urlpatterns = [
    path("contacto-detailing", detailing_index, name="detailing.index"),
    path("contacto-detailing/store", detailing_store, name="detailing.store"),
    path("carro/index", carro_index, name="carro.index"),
    path("carro/store", carro_store, name="carro.store"),
    path("carro/delete/<int:id>", carro_delete, name="carro.delete"),
    path("carro/update/<int:id>", carro_update, name="carro.update"),
]
