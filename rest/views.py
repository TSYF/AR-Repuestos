from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from django.views.decorators.csrf import csrf_exempt
from core.models import Cliente, Servicio, ContactoServicio
from .serializers import ClienteSerializer, ServicioSerializer, ContactoServicioSerializer, ContactoServicioReadSerializer, ContactoServicioWriteSerializer


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
