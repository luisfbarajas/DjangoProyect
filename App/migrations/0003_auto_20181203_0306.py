# Generated by Django 2.1.3 on 2018-12-03 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20181203_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividades',
            name='encargado',
            field=models.ForeignKey(default='unassigned', on_delete=django.db.models.deletion.CASCADE, to='App.empleados'),
        ),
    ]