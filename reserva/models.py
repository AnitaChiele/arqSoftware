from django.db import models
from django.utils.translation import gettext as _l
# from django.core.validators import MinValueValidator
from quartos.models import Quarto
from pessoas.models import Cliente


class StatusReserva(models.Model):

    class Meta:
        verbose_name = 'Status do reserva'
        verbose_name_plural = 'Status dos reservas'

    def __str__(self):
        return str(self.descricao)

    descricao = models.CharField(
        verbose_name=_l("Descrição"),
        max_length=255
    )


class Reserva(models.Model):

    class Meta:
        verbose_name = _l('Reserva')
        verbose_name_plural = _l('Reservas')

    def __str__(self):
        return str(self.pk)

    quarto = models.ForeignKey(
        Quarto,
        on_delete=models.PROTECT
    )

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT
    )

    data_entrada = models.DateField()
    data_saida = models.DateField()

    hora_checkin = models.TimeField(
        blank=True,
        null=True
    )

    hora_checkout = models.TimeField(
        blank=True,
        null=True
    )

    status = models.ForeignKey(
        StatusReserva,
        on_delete=models.PROTECT
    )
