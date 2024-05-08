# Generated by Django 5.0.6 on 2024-05-08 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyectos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('tecnologia', models.CharField(max_length=50)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
