# Generated by Django 5.0.6 on 2024-07-13 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_tipousuario'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TipoUsuario',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='id_genero',
        ),
    ]