# Generated by Django 5.0.3 on 2024-03-17 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tp1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='aoellido',
            new_name='apellido',
        ),
    ]
