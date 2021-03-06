# Generated by Django 2.2.6 on 2019-11-06 01:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StatusCliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Status do cliente',
                'verbose_name_plural': 'Status dos clientes',
            },
        ),
        migrations.CreateModel(
            name='StatusFuncionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Status do funcionário',
                'verbose_name_plural': 'Status dos funcionários',
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('data_nascimento', models.DateField()),
                ('cpf', models.CharField(max_length=11)),
                ('telefone', models.CharField(max_length=11)),
                ('enedereco', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('cargo', models.CharField(max_length=250)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.01)], verbose_name='Salário')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pessoas.StatusFuncionario', verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Funcionário',
                'verbose_name_plural': 'Funcionários',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('data_nascimento', models.DateField()),
                ('cpf', models.CharField(max_length=11)),
                ('telefone', models.CharField(max_length=11)),
                ('enedereco', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('data_registro', models.DateField()),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pessoas.StatusCliente', verbose_name='Status do Cliente')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]
