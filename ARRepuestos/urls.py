"""
URL configuration for ARRepuestos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import home, detailing, tienda, producto, trabajos, sign_in, sign_up

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="inicio"),
    path("tienda", tienda, name="tienda"),
    path("producto", producto, name="producto"),
    path("trabajos", trabajos, name="trabajos"),
    path("detailing", detailing, name="detailing"),
    path("signIn", sign_in, name="signIn"),
    path("signUp", sign_up, name="signUp"),
]
