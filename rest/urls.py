from django.urls import path
from .views import detailing_store, detailing_index, carro_index, carro_store, carro_delete, carro_update, orden_store, get_user, signin_user, signout_user, signup_user

urlpatterns = [
    path("contacto-detailing", detailing_index, name="detailing.index"),
    path("contacto-detailing/store", detailing_store, name="detailing.store"),
    path("carro/index", carro_index, name="carro.index"),
    path("carro/store", carro_store, name="carro.store"),
    path("carro/delete/<int:id>", carro_delete, name="carro.delete"),
    path("carro/update/<int:id>", carro_update, name="carro.update"),
    path("orden/buy", orden_store, name="orden.store"),
    path("auth", get_user, name="auth"),
    path("auth/signUp", signup_user, name="auth.signup"),
    path("auth/signIn", signin_user, name="auth.signin"),
    path("auth/signOut", signout_user, name="auth.signout")
]
