from django.db import models


class Importacao(models.Model):

    class Meta:
        verbose_name = 'Importação'
        verbose_name_plural = 'Importações'

    def __str__(self):
        return "%s" % (self.arquivo)

    arquivo = models.FileField(
        upload_to='produtos/',
        blank=True,
        null=True
    )
