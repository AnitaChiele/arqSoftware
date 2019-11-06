from django.contrib import admin
from .models import StatusReserva, Reserva
from django.utils.translation import gettext as _l

admin.site.register(StatusReserva)


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = (
        'numero_reserva', 'nome_cliente', 'numero_quarto', 'situacao_reserva'
    )

    def numero_reserva(self, obj):
        return obj.pk
    numero_reserva.short_description = _l('Número')
    numero_reserva.admin_order_field = 'pk'

    def nome_cliente(self, obj):
        return obj.cliente.nome
    nome_cliente.short_description = _l('Cliente')
    nome_cliente.admin_order_field = 'cliente'

    def numero_quarto(self, obj):
        return obj.quarto.numero
    numero_quarto.short_description = _l('Quarto')
    numero_quarto.admin_order_field = 'numero'

    def situacao_reserva(self, obj):
        return obj.status.descricao
    situacao_reserva.short_description = _l('Status')
    situacao_reserva.admin_order_field = 'descricao'
