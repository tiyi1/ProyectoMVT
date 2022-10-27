# Generated by Django 4.1.2 on 2022-10-27 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
                ('apellido', models.CharField(max_length=10)),
                ('fecha_de_nacimiento', models.DateField()),
                ('contacto_tel', models.PositiveIntegerField()),
                ('contacto_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
                ('apellido', models.CharField(max_length=10)),
                ('fecha_de_nacimiento', models.DateField()),
                ('contacto_tel', models.PositiveIntegerField()),
                ('contacto_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empresa', models.CharField(max_length=10)),
                ('contacto_tel', models.PositiveIntegerField()),
                ('contacto_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
