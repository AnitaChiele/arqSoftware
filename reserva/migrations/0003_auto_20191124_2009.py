# Generated by Django 2.2.6 on 2019-11-24 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0002_reserva_preco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='cliente',
            field=models.ForeignKey(limit_choices_to={'status__descricao': 'Ativo'}, on_delete=django.db.models.deletion.PROTECT, to='pessoas.Cliente'),
        ),
    ]
