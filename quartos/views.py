from django.core import serializers
from django.http import HttpResponse
from .models import Quarto


def limpar(request):
    quartos = Quarto.objects.filter(
        status__descricao="Limpar"
    )

    json_quartos = serializers.serialize('json', quartos)
    return HttpResponse(json_quartos, content_type='application/json')
