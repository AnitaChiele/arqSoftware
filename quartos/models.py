from django.db import models
from django.utils.translation import gettext as _l
from django.core.validators import MinValueValidator


class StatusQuarto(models.Model):

    class Meta:
        verbose_name = 'Status do quarto'
        verbose_name_plural = 'Status dos quartos'

    def __str__(self):
        return str(self.descricao)

    descricao = models.CharField(
        verbose_name=_l("Descrição"),
        max_length=255
    )


class Quarto(models.Model):

    class Meta:
        verbose_name = _l('Quarto')
        verbose_name_plural = _l('Quartos')

    def __str__(self):
        return str(self.numero)

    numero = models.IntegerField(
        verbose_name=_l('Número do quarto'),
        validators=[MinValueValidator(1)]
    )

    status = models.ForeignKey(
        StatusQuarto,
        verbose_name=_l('Situação do quarto'),
        on_delete=models.PROTECT
    )


class TipoCama(models.Model):

    class Meta:
        verbose_name = 'Tipo da cama'
        verbose_name_plural = 'Tipos da cama'

    def __str__(self):
        return str(self.descricao)

    descricao = models.CharField(
        verbose_name=_l("Descrição"),
        max_length=255
    )


class CamaQuarto(models.Model):

    class Meta:
        verbose_name = 'Camas do quarto'
        verbose_name_plural = 'Camas dos quartos'

    def __str__(self):
        return str(self.quarto)

    quarto = models.ForeignKey(
        Quarto,
        on_delete=models.PROTECT
    )

    tipo_cama = models.ForeignKey(
        TipoCama,
        verbose_name=_l('Tipo da cama'),
        on_delete=models.PROTECT
    )

    quantidade = models.IntegerField(
        validators=[MinValueValidator(1)],
        default=1
    )
