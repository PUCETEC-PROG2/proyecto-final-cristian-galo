import django.core.validators
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
                ('nombre_categoria', models.CharField(max_length=100)),
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
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=200)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=7)),
                ('descripcion', models.TextField(max_length=500)),
                ('talla', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=50)),
                ('material', models.CharField(max_length=100)),
                ('imagen', models.ImageField(upload_to='ropa_images')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='catalogo_ropa.categoria')),
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
                ('productos', models.ManyToManyField(to='catalogo_ropa.producto')),
            ],
        ),
    ]