from django.contrib import admin
from .models import StatusCliente, StatusFuncionario, Funcionario, Cliente

admin.site.register(StatusCliente)
admin.site.register(StatusFuncionario)
admin.site.register(Funcionario)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'nome', 'cpf', 'telefone', 'status'
    )

    ordering = ('-nome', 'status')
