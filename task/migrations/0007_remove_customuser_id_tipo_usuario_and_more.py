# Generated by Django 5.0.6 on 2024-07-14 23:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_customuser_id_tipo_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='ID_tipo_usuario',
        ),
        migrations.AddField(
            model_name='customuser',
            name='id_genero',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='task.generocliente'),
        ),
        migrations.DeleteModel(
            name='TipoUsuario',
        ),
    ]