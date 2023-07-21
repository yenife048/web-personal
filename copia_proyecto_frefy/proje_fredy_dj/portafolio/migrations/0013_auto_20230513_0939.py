# Generated by Django 3.2.7 on 2023-05-13 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0012_auto_20230513_0934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='red',
            name='link_redes',
        ),
        migrations.AddField(
            model_name='red',
            name='link_redes1',
            field=models.URLField(blank=True, null=True, verbose_name='Direccion Web Email'),
        ),
        migrations.AddField(
            model_name='red',
            name='link_redes2',
            field=models.URLField(blank=True, null=True, verbose_name='Direccion Web Git'),
        ),
        migrations.AddField(
            model_name='red',
            name='link_redes3',
            field=models.URLField(blank=True, null=True, verbose_name='Direccion Web Youtube'),
        ),
    ]
