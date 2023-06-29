# Generated by Django 4.2.2 on 2023-06-17 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_idcategoria_categoria_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoProducto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de estado del producto')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre del estado del producto')),
            ],
            options={
                'verbose_name': 'estado del producto',
                'verbose_name_plural': 'estados del producto',
            },
        ),
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(default=models.CharField(max_length=50, verbose_name='Nombre de producto'), max_length=100, verbose_name='Descripción corta del producto'),
        ),
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(default=0, verbose_name='Cantidad del producto en stock'),
        ),
        migrations.AddField(
            model_name='producto',
            name='texto',
            field=models.TextField(default=models.CharField(max_length=50, verbose_name='Nombre de producto'), verbose_name='Descripciión larga del produucto'),
        ),
        migrations.AddField(
            model_name='producto',
            name='estado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.estadoproducto', verbose_name='estado del producto'),
        ),
    ]
