from django.shortcuts import render

# Create your views here.

def home(request):
    # return HttpResponse("Hola desde Django")
    return render(request, "index.html")

def tienda(request):
    return render(request, "tienda.html")

def producto(request):
    return render(request, "producto.html")

def detailing(request):
    return render(request, "detailing.html")

def trabajos(request):
    return render(request, "trabajos.html")

def sign_in(request):
    return render(request, "signIn.html")

def sign_up(request):
    return render(request, "signUp.html")