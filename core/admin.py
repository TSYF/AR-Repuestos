from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Categoria)
admin.site.register(models.Producto)
admin.site.register(models.EstadoProducto)
admin.site.register(models.Servicio)
admin.site.register(models.Cliente)
admin.site.register(models.ContactoServicio)