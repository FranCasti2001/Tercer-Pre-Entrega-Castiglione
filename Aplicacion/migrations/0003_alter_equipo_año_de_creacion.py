# Generated by Django 4.2 on 2023-04-25 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0002_rename_apodo_equipo_apodo_rename_dt_equipo_dt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='Año_de_Creacion',
            field=models.IntegerField(),
        ),
    ]
