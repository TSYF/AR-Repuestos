from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from core.models import ContactoServicio, Orden
from .serializers import (ContactoServicioReadSerializer, ContactoServicioWriteSerializer,
    OrdenSerializer, ProductoOrdenSerializer, UserSerializer)
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework import views
from .utils import construct_drf_response


class DetailingAPIView(views.APIView):

    def get(self, request, id=None):
        
        forms_serializer = None

        if id is None:
            forms = ContactoServicio.objects.all()
            forms_serializer = ContactoServicioReadSerializer(forms, many=True)
        else:
            form = ContactoServicio.objects.get(id=id)
            forms_serializer = ContactoServicioReadSerializer(form)
            
        return construct_drf_response(forms_serializer.data, 200)

    @method_decorator(csrf_exempt)
    def post(self, request, id=None):
        
        data = request.data
        
        nombre = data["nombre"]
        rut = data["rut"].split("-")
        telefono = data["telefono"]
        email = data["email"]

        numrut = rut[0]
        dvrut = rut[1]
        

        cliente = {
            "nombre"  : nombre,
            "numrut"  : numrut,
            "dvrut"   : dvrut,
            "telefono": telefono,
            "email"   : email
        }
        
        form = {
            "cliente" : cliente,
            "servicio": data["servicio"]
        }

        form_serializer = ContactoServicioWriteSerializer(data=form)
        
        if form_serializer.is_valid():
            form_serializer.save()
            return construct_drf_response(form_serializer.data, 201)
        else:
            return construct_drf_response(form_serializer.errors, 400)


class CarroAPIView(views.APIView):
    
    def get(self, request, id=None):
        
        carro_list = request.session.get("carro", [])
        
        if id is None:
            return construct_drf_response(carro_list, 200)
        
        try:

            id = int(id)
            item = carro_list[id]
            return construct_drf_response(item, 200)
            
        except (ValueError, IndexError):
            return construct_drf_response("ID must be an integer", 400)

    def post(self, request, id=None):
        
        producto = request.data

        if request.session.get("carro", False):
            request.session["carro"] = []

        request.session["carro"].append(producto)
        
        return construct_drf_response(request.session["carro"][-1], 201)

    def delete(self, request, id):

        try:
            id = int(id)
        except:
            return construct_drf_response("ID must be an integer", 400)
        
        if not request.session.get("carro", False):
                    request.session["carro"] = []
        
        carro = request.session["carro"]
        
        request.session["carro"] = [ item for item in carro if item["id"] != id ]

        return construct_drf_response(carro, 200)

    def patch(self, request, id):

        try:
            id = int(id)
        except:
            return construct_drf_response("ID must be an integer", 400)
        
        if not request.session.get("carro", False):
            request.session["carro"] = []
        
        carro = request.session["carro"]
        
        for i, item in enumerate(carro):
            if item["id"] == id:
                print(item["id"] == id)
                for key, value in request.data.items():
                    if key == "cantidad":
                        carro[i]["subtotal"] = carro[i]["precio"] * value
                    
                    carro[i][key] = value
        
        request.session["carro"] = carro

        return construct_drf_response(carro, 200)


@api_view(["GET"])
def orden_index(request):
    ordenes = Orden.objects.all()
    
    ordenes_data = OrdenSerializer(ordenes, many=True).data
    
    return construct_drf_response(ordenes_data, 200)

@api_view(["POST"])
def orden_store(request):

    data = request.data

    orden = {
        "productos": [prod["id"] for prod in data],
        "estado_pago": True
    }

    
    orden_serializer = OrdenSerializer(data=orden)


    if orden_serializer.is_valid():
        orden_instance = orden_serializer.save()
        producto_orden = [{"producto": producto["id"], "orden": orden_instance.id, "cantidad": producto["cantidad"]} for producto in data ]
        producto_orden_serializer = ProductoOrdenSerializer(data=producto_orden, many=True)

        if producto_orden_serializer.is_valid():
            orden_instance = orden_serializer.save()
            producto_orden_serializer.save()

            request.session["carro"] = []
            
            # return Response(orden_serializer.data, status.HTTP_200_OK)
            return construct_drf_response(orden_serializer.data, 200)
        else:
            return construct_drf_response(producto_orden_serializer.errors, 400)
    else:
        return construct_drf_response(orden_serializer.errors, 400)
    
    
@api_view(["POST"])
def signup_user(request):
    
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid():    
        serializer.save()
        return construct_drf_response(serializer.data, 201)

    return construct_drf_response(serializer.errors, 400)
        

@api_view(["POST"])
def signin_user(request):
    
    if request.user.is_authenticated:
        return construct_drf_response('User already authenticated', 200)

    username = request.data["username"]
    password = request.data["password"]
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        serializer = UserSerializer(user)
        return construct_drf_response(serializer.data, 200)
    else:
        return construct_drf_response('Invalid username or password', 401)


@api_view(["GET"])
def get_user(request):
    if not request.user.is_authenticated:
        return construct_drf_response('User not authenticated', 401)

    serializer = UserSerializer(request.user)
    return construct_drf_response(serializer.data, 200)


@api_view(["GET"])
def signout_user(request):
    if not request.user.is_authenticated:
        return construct_drf_response('User not authenticated', 401)

    logout(request)
    return construct_drf_response('User logged out', 200)