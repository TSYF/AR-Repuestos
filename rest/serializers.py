from rest_framework import serializers
from core.models import Cliente, Servicio, ContactoServicio, Orden, Producto, ProductoOrden


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = (
            'id',
            'nombre',
            'telefono',
            'email',
            "numrut",
            "dvrut"
        )

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = (
            "id",
            "nombre"
        )
        
class ContactoServicioSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactoServicio
        fields = "__all__"


class ContactoServicioReadSerializer(ContactoServicioSerializer):
    cliente = ClienteSerializer(read_only=True)
    servicio = ServicioSerializer(read_only=True)

    class Meta:
        model = ContactoServicio
        fields = [
            "id",
            "cliente",
            "servicio"
        ]
    
class ContactoServicioWriteSerializer(ContactoServicioSerializer):
    cliente = ClienteSerializer(read_only=False)
    # servicio = ServicioSerializer(read_only=False)

    class Meta:
        model = ContactoServicio
        fields = [
            "id",
            "cliente",
            "servicio"
        ]

    def create(self, validated_data):
        cliente_data = validated_data.pop('cliente')
        # servicio_data = validated_data.pop('servicio')
        servicio = validated_data.pop('servicio')

        cliente, created = Cliente.objects.get_or_create(**cliente_data)
        # servicio = Servicio.objects.get(**servicio_data)

        formulario_contacto = ContactoServicio.objects.create(
            cliente=cliente,
            servicio=servicio,
            **validated_data
        )

        return formulario_contacto
    
    
class OrdenSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Orden
        fields = [
            "id",
            "productos",
            "estado_pago"
        ]
        

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"

class ProductoOrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoOrden
        fields = "__all__"