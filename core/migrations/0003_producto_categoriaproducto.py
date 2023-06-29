# Generated by Django 4.2.2 on 2023-06-17 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_producto_precioproducto_alter_producto_idproducto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='categoriaProducto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='core.categoria', verbose_name='Id de categoría'),
            preserve_default=False,
        ),
    ]