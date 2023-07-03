from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Producto, ContactoServicio, Cliente, Servicio
from .forms import ProductoForm

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
    productoForm = ProductoForm(producto.__dict__)

    data = {
        "producto": producto,
        "form": productoForm
    }
    match request.method:
        case 'GET':
            if not request.session.get("carro", False):
                request.session["carro"] = []
            
            pass            
        
        case 'POST':
            carro = request.session["carro"]
            
            producto = {
                "id": int(request.POST["id"]),
                "nombre": request.POST["nombre"],
                "precio": int(request.POST["precio"]),
                "categoria": request.POST["categoria"],
                "estado": request.POST["estado"],
                "cantidad": 1,
                "subtotal": int(request.POST["precio"]),
            }
            

            item_in_carro_index = None

            for i, item in enumerate(carro):
                if item["id"] == producto["id"]:
                    item_in_carro_index = i
            
            if item_in_carro_index != None:
                carro[i]["cantidad"] += 1
                carro[i]["subtotal"] += carro[i]["precio"]
            else:
                carro.append(producto)

            request.session["carro"] = carro

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


def carro_show(request):

    carro = request.session["carro"]

    total = 0

    for item in carro:
        total += item["subtotal"]

    data = {
        "carro": carro,
        "total": total
    }
    return render(request, "carro.html", data)