# Generated by Django 5.0.3 on 2024-03-17 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Marca', models.CharField(max_length=20)),
                ('Modelo', models.CharField(max_length=30)),
                ('Color', models.CharField(max_length=50)),
            ],
        ),
    ]
