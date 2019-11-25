from django.db import models
from django.utils.translation import gettext as _l
from django.core.validators import MinValueValidator


class StatusCliente(models.Model):

    class Meta:
        verbose_name = 'Status do cliente'
        verbose_name_plural = 'Status dos clientes'

    def __str__(self):
        return str(self.descricao)

    descricao = models.CharField(
        verbose_name=_l("Descrição"),
        max_length=255
    )


class StatusFuncionario(models.Model):

    class Meta:
        verbose_name = 'Status do funcionário'
        verbose_name_plural = 'Status dos funcionários'

    def __str__(self):
        return str(self.descricao)

    descricao = models.CharField(
        verbose_name=_l("Descrição"),
        max_length=255
    )


class Cliente(models.Model):

    class Meta:
        verbose_name = _l('Cliente')
        verbose_name_plural = _l('Clientes')

    def __str__(self):
        return str(self.nome)

    nome = models.CharField(
        max_length=150
    )

    data_nascimento = models.DateField(
        blank=True,
        null=True
    )

    cpf = models.CharField(
        max_length=110
    )

    telefone = models.CharField(
        max_length=110
    )

    enedereco = models.CharField(
        max_length=250
    )

    email = models.CharField(
        max_length=250
    )

    status = models.ForeignKey(
        StatusCliente,
        verbose_name=_l('Status do Cliente'),
        on_delete=models.PROTECT
    )


class Funcionario(models.Model):

    class Meta:
        verbose_name = _l('Funcionário')
        verbose_name_plural = _l('Funcionários')

    def __str__(self):
        return str(self.nome)

    nome = models.CharField(
        max_length=150
    )

    data_nascimento = models.DateField()

    cpf = models.CharField(
        max_length=11
    )

    telefone = models.CharField(
        max_length=11
    )

    enedereco = models.CharField(
        max_length=250
    )

    email = models.CharField(
        max_length=250
    )

    cargo = models.CharField(
        max_length=250
    )

    salario = models.DecimalField(
        verbose_name=_l('Salário'),
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )

    status = models.ForeignKey(
        StatusFuncionario,
        verbose_name=_l('Status'),
        on_delete=models.PROTECT
    )
