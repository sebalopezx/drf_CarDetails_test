# Generated by Django 4.1.13 on 2023-12-04 20:38

import app.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarMarca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=255, unique=True, verbose_name='Marca')),
                ('slugmarca', models.SlugField(blank=True, unique=True, verbose_name='Slug Marca')),
            ],
        ),
        migrations.CreateModel(
            name='CarModelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=255, unique=True, verbose_name='Modelo')),
                ('slugmodelo', models.SlugField(blank=True, unique=True, verbose_name='Slug Modelo')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.carmarca', verbose_name='Id Marca')),
            ],
        ),
        migrations.CreateModel(
            name='CarAnio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField(max_length=4, validators=[app.models.validate_year, django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(limit_value=9999)], verbose_name='Año')),
                ('car_marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.carmarca', verbose_name='Id Marca')),
                ('car_modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.carmodelo', verbose_name='Id Modelo')),
            ],
            options={
                'unique_together': {('car_marca', 'car_modelo', 'anio')},
            },
        ),
    ]