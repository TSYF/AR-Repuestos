# Generated by Django 4.2.2 on 2023-06-17 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_estadoproducto_producto_descripcion_producto_stock_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(verbose_name='Precio de producto'),
        ),
    ]