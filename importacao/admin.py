import csv
from django.contrib import admin
from importacao.models import Importacao
from pessoas.models import Cliente, StatusCliente


@admin.register(Importacao)
class ImportacaoAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        arquivo = obj.arquivo.path

        with open(arquivo) as f:
            reader = csv.reader(
                f,
                delimiter=","
            )

            for i, row in enumerate(reader):
                if i > 0:
                    cliente = Cliente()
                    cliente.pk = row[0]
                    cliente.nome = row[1]
                    cliente.data_nascimento = row[2]
                    cliente.cpf = row[3]
                    cliente.telefone = row[4]
                    cliente.endereco = row[5]
                    cliente.email = row[6]
                    cliente.data_registro = row[7]

                    pk_status = int(row[8]) + 1

                    status_cliente = StatusCliente.objects.filter(
                        pk=pk_status
                    ).first()

                    cliente.status_id = status_cliente.pk
                    cliente.save()
