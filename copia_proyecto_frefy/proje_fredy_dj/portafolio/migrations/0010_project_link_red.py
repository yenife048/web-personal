# Generated by Django 3.2.7 on 2023-05-13 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0009_alter_project_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link_red',
            field=models.URLField(blank=True, null=True, verbose_name='Direccion redes sociales'),
        ),
    ]
