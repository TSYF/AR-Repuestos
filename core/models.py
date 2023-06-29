from django.db import models
from django.core.validators import MaxValueValidator

class Categoria(models.Model):

    id = models.AutoField("Id de categoría", primary_key=True)
    nombre = models.CharField("Nombre de categoría", max_length=30)

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"


class Producto(models.Model):

    id = models.AutoField("Id de producto", primary_key=True)
    categoria = models.ForeignKey("core.categoria", verbose_name="Id de categoría", on_delete=models.RESTRICT)
    nombre = models.CharField("Nombre de producto", max_length=50)
    precio = models.PositiveIntegerField("Precio de producto")
    img = models.CharField("Dirección de la imagen del producto desde static/core/img/", max_length=50)
    descripcion = models.CharField("Descripción corta del producto", max_length=100, null=True)
    texto = models.TextField("Descripciión larga del produucto", null=True)
    stock = models.PositiveIntegerField("Cantidad del producto en stock", default=0)
    estado = models.ForeignKey("core.EstadoProducto", verbose_name="estado del producto", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"


class EstadoProducto(models.Model):

    id = models.AutoField("Id de estado del producto", primary_key=True)
    nombre = models.CharField("Nombre del estado del producto", max_length=30)
    
    class Meta:
        verbose_name = "estado del producto"
        verbose_name_plural = "estados del producto"
        

class Servicio(models.Model):
    
    id = models.AutoField("Id del servicio", primary_key=True)
    nombre = models.CharField("Nombre del servicio", max_length=50)
    

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"

        
class Cliente(models.Model):

    id = models.AutoField("Id del cliente", primary_key=True)
    numrut = models.IntegerField("Número del RUT del cliente", validators=[MaxValueValidator(99999999)])
    dvrut = models.CharField("Dígito Verificador del RUT del cliente", max_length=1)
    nombre = models.CharField("Nombre del cliente", max_length=100)
    telefono = models.PositiveIntegerField("Número de teléfono de contacto del cliente", validators=[MaxValueValidator(999999999)])
    email = models.CharField("Email de contacto del cliente", max_length=256)

    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"

        
class ContactoServicio(models.Model):

    # TODO: Modificar formulario para coincidir con el modelo
    id = models.AutoField("Id de los datos de contacto", primary_key=True)
    cliente = models.ForeignKey("core.Cliente", verbose_name="ID del cliente", null=True, on_delete=models.SET_NULL)
    servicio = models.ForeignKey("core.Servicio", verbose_name="ID del servicio solicitado", null=True, on_delete=models.SET_NULL)
    
    class Meta:
        db_table = "core_cliente_servicio"
        verbose_name = "cliente servicio"
        verbose_name_plural = "cliente servicio"
    