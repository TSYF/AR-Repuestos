from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Producto, ContactoServicio, Cliente, Servicio

# Create your views here.

def home(request):
    return render(request, "index.html")

def tienda(request, page = 1):
    limit = 6
    
    productos = Producto.objects.all()

    paginator = Paginator(productos, limit)

    data = {
        "page": paginator.get_page(page)
    }

    return render(request, "tienda.html", data)

def producto(request, id):

    producto = Producto.objects.get(id=id)

    data = {
        "producto": producto
    }
    
    return render(request, "producto.html", data)

def detailing_create(request):
    data = {
        'form': ContactoServicio()
    }

    if (request.method == 'GET'):
        
        data["servicios"] = Servicio.objects.all()

    return render(request, "detailing.html", data)

def trabajos(request):
    return render(request, "trabajos.html")

def sign_in(request):
    return render(request, "signIn.html")

def sign_up(request):
    return render(request, "signUp.html")
