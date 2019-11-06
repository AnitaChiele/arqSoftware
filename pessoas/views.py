from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def clientes_importacao(request):
    template = loader.get_template('clientes_importacao.html')

    print("\n" * 5)
    print(template)

    context = {
        'teste': 1,
    }

    return HttpResponse(template.render(context, request))


def clientes_import_file(request):
    arquivo = request.POST.get('arquivo_importacao')
    print(arquivo)
