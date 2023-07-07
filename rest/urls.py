from django.urls import path, re_path
from .views import (
    CarroAPIView,
    DetailingAPIView,
    get_user,
    orden_store,
    signin_user,
    signout_user,
    signup_user
)

urlpatterns = [
    re_path("detailing/((?P<id>\d+)/)?$", DetailingAPIView.as_view(), name="detailing"),
    re_path("carro/((?P<id>\d+)/)?$", CarroAPIView.as_view(), name="carro"),
    path("orden/buy/", orden_store, name="orden.store"),
    path("auth/", get_user, name="auth"),
    path("auth/signUp/", signup_user, name="auth.signup"),
    path("auth/signIn/", signin_user, name="auth.signin"),
    path("auth/signOut/", signout_user, name="auth.signout")
]
