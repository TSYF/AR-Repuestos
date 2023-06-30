# Generated by Django 4.2.2 on 2023-06-17 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precioProducto',
            field=models.IntegerField(default=0, max_length=10, verbose_name='Precio de producto'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='idProducto',
            field=models.AutoField(max_length=50, primary_key=True, serialize=False, verbose_name='Id de producto'),
        ),
    ]
