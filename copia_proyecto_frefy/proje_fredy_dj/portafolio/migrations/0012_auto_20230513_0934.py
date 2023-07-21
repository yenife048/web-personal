# Generated by Django 3.2.7 on 2023-05-13 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0011_auto_20230513_0925'),
    ]

    operations = [
        migrations.CreateModel(
            name='red',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_redes', models.URLField(blank=True, null=True, verbose_name='Direccion Web')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha Actualizado')),
            ],
        ),
        migrations.DeleteModel(
            name='redes',
        ),
    ]