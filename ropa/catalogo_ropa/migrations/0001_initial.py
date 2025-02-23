# Generated by Django 4.2 on 2025-02-11 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(max_length=100, verbose_name='Nombre de la Categoría')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('apellidos', models.CharField(max_length=150)),
                ('cedula', models.BigIntegerField()),
                ('telefono', models.BigIntegerField()),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad', models.CharField(max_length=50)),
                ('fecha_compra', models.DateField()),
                ('precio_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='catalogo_ropa.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=200)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descripcion', models.TextField()),
                ('talla', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('material', models.CharField(max_length=100)),
                ('imagen', models.ImageField(upload_to='productos/')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo_ropa.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='catalogo_ropa.compra')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo_ropa.producto')),
            ],
        ),
        migrations.AddField(
            model_name='compra',
            name='productos',
            field=models.ManyToManyField(to='catalogo_ropa.producto'),
        ),
    ]
