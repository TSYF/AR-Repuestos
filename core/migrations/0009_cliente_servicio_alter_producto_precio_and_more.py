# Generated by Django 4.2.2 on 2023-06-19 03:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_producto_descripcion_alter_producto_texto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id del cliente')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del cliente')),
                ('telefono', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999999999)], verbose_name='Número de teléfono de contacto del cliente')),
                ('email', models.CharField(max_length=256, verbose_name='Email de contacto del cliente')),
            ],
            options={
                'verbose_name': 'cliente',
                'verbose_name_plural': 'clientes',
            },
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id del servicio')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre del servicio')),
            ],
            options={
                'verbose_name': 'servicio',
                'verbose_name_plural': 'servicios',
            },
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.PositiveIntegerField(verbose_name='Precio de producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='stock',
            field=models.PositiveIntegerField(default=0, verbose_name='Cantidad del producto en stock'),
        ),
        migrations.CreateModel(
            name='FormularioContacto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de los datos de contacto')),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.cliente', verbose_name='ID del cliente')),
                ('servicio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.servicio', verbose_name='ID del servicio solicitado')),
            ],
            options={
                'verbose_name': 'formulario de contacto',
                'verbose_name_plural': 'formularios de contacto',
            },
        ),
    ]
