# Generated by Django 3.2.7 on 2023-05-25 20:13

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0004_auto_20230525_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenidos_empresa',
            name='contenido',
            field=ckeditor.fields.RichTextField(verbose_name='Contenido_Mision'),
        ),
    ]
