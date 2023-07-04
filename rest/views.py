from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from django.views.decorators.csrf import csrf_exempt
from core.models import ContactoServicio, Orden
from .serializers import (ContactoServicioReadSerializer, ContactoServicioWriteSerializer,
    OrdenSerializer, ProductoOrdenSerializer, UserSerializer)
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.forms.models import model_to_dict


# ACTUALMENTE SIN USO.
@api_view(["GET"])
def detailing_index(request):
    
    forms = ContactoServicio.objects.all()

    forms_serializer = ContactoServicioReadSerializer(forms, many=True)

    return Response(forms_serializer.data, status=status.HTTP_200_OK)
    

# @csrf_exempt
@api_view(["POST"])
def detailing_store(request):
    
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
        return Response(form_serializer.data, status.HTTP_201_CREATED)
    else:
        return Response(form_serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def orden_index(request):
    ordenes = Orden.objects.all()
    
    ordenes_data = OrdenSerializer(ordenes, many=True).data
    
    return Response(ordenes_data, status.HTTP_200_OK)


@api_view(["GET"])
def carro_index(request):
    
    return Response( request.session.get("carro", []), status.HTTP_200_OK )

@api_view(["POST"])
def carro_store(request):
    
    producto = request.data

    if request.session.get("carro", False):
        request.session["carro"] = []

    request.session["carro"].append(producto)
    
    return Response(
        {
            "carro": request.session["carro"][-1],
            "status": "OK"
        },
        status.HTTP_200_OK
    )

@csrf_exempt
@api_view(["DELETE"])
def carro_delete(request, id):
    
    if not request.session.get("carro", False):
                request.session["carro"] = []
    
    carro = request.session["carro"]
    
    request.session["carro"] = [ item for item in carro if item["id"] != id ]

    return Response(carro, status.HTTP_200_OK)


@csrf_exempt
@api_view(["PATCH"])
def carro_update(request, id):
    
    if not request.session.get("carro", False):
                request.session["carro"] = []
    
    carro = request.session["carro"]
    
    for i, item in enumerate(carro):
        if item["id"] == id:
            for key, value in request.data.items():
                if key == "cantidad":
                    carro[i]["subtotal"] = carro[i]["precio"] * value
                
                carro[i][key] = value
    
    request.session["carro"] = carro

    return Response(carro, status.HTTP_200_OK)


@csrf_exempt
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
            
            return Response(orden_serializer.data, status.HTTP_200_OK)
        else:
            return Response(producto_orden_serializer.errors, status.HTTP_400_BAD_REQUEST)
    else:
        return Response(orden_serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    
@api_view(["POST"])
def signup_user(request):
    
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid():    
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        

@api_view(["POST"])
def signin_user(request):
    
    if request.user.is_authenticated:
        return Response({'message': 'User already authenticated.'}, status=status.HTTP_400_BAD_REQUEST)

    username = request.data["username"]
    password = request.data["password"]
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Invalid username or password.'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(["GET"])
def get_user(request):
    if not request.user.is_authenticated:
        return Response({'message': 'User not authenticated.', "status": 401}, status=status.HTTP_401_UNAUTHORIZED)

    serializer = UserSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def signout_user(request):
    if not request.user.is_authenticated:
        return Response({'message': 'User not authenticated.', "status": 401}, status=status.HTTP_401_UNAUTHORIZED)

    logout(request)
    return Response({'message': 'User logged out.'}, status=status.HTTP_200_OK)