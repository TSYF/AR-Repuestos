from django.urls import path, include
from .views import home, detailing_create, tienda, producto, trabajos, sign_in, sign_up, carro_show

urlpatterns = [
    path("", home, name="inicio"),
    path("tienda/", tienda, name="tienda"),
    path("tienda/page/<int:page>/", tienda, name="tienda.page"),
    path("producto/<int:id>/", producto, name="producto"),
    path("trabajos/", trabajos, name="trabajos"),
    path("contacto-detailing/create/", detailing_create, name="detailing.create"),
    path("signIn/", sign_in, name="signIn"),
    path("signUp/", sign_up, name="signUp"),
    path("carro/", carro_show, name="carro.show")
]
