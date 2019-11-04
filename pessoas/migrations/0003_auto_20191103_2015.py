# Generated by Django 2.2.6 on 2019-11-03 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0002_auto_20191103_2014'),
    ]

    operations = [
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
        migrations.AlterField(
            model_name='funcionario',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pessoas.StatusFuncionario', verbose_name='Status'),
        ),
    ]
