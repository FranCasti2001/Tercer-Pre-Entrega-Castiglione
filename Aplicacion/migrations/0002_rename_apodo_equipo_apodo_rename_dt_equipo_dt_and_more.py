# Generated by Django 4.2 on 2023-04-25 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipo',
            old_name='apodo',
            new_name='Apodo',
        ),
        migrations.RenameField(
            model_name='equipo',
            old_name='dt',
            new_name='Dt',
        ),
        migrations.RenameField(
            model_name='equipo',
            old_name='nombre',
            new_name='Nombre',
        ),
        migrations.AlterField(
            model_name='equipo',
            name='Año_de_Creacion',
            field=models.CharField(max_length=30),
        ),
    ]