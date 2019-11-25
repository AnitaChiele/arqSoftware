# Generated by Django 2.2.6 on 2019-11-11 23:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=0.01, max_digits=10, validators=[django.core.validators.MinValueValidator(0.01)], verbose_name='Preço'),
            preserve_default=False,
        ),
    ]