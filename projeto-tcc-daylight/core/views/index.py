# -*- coding: utf-8 -*-
import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from core.models.pedidomodel import Pedido
from core.models.compramodel import Compra
from core.models.servicomodel import Servico
import requests
from core.views.expedicaoview import expedicao


@login_required(login_url='/entrar')
def index(request):

    temperatura = None
    clima = None
    icone_previsao = None
    cidade = None

    data_agora = datetime.datetime.now()

    qtd_pedidos = Pedido.objects.filter(status='Em andamento').count()
    qtd_compras = Compra.objects.filter(status='Em andamento').count()
    qtd_servicos = Servico.objects.filter(status='Em andamento').count()

    # lista os pedidos disponiveis para entrega
    pronto_entrega = {}
    validacao_status = []

    serv_finalizado = Servico.objects.filter(status='Finalizado')
    for entrega in serv_finalizado:
        pedido = entrega.numero_pedido

        qtd = Servico.objects.filter(numero_pedido=pedido).count()
        if qtd >= 1:
            confere = Servico.objects.filter(numero_pedido=pedido)
            for obj_confere in confere:
                if obj_confere.status == 'Finalizado':
                    validacao_status.append('ok')
                else:
                    validacao_status.append('erro')

        if 'erro' in validacao_status:
            validacao_status.clear()

        else:
            validacao_status.clear()
            lista_pedido = Pedido.objects.filter(numero_pedido=str(pedido))
            for item in lista_pedido:
                if item.status == 'Em andamento':
                    pronto_entrega[pedido] = lista_pedido
    
    qtd_expedicao = len(pronto_entrega)

    try:
        apiadvisor = "http://apiadvisor.climatempo.com.br/api/v1/weather/locale/{id}/current?token={token}".format(id="3735", token="b7318a88ccb10c96eae3a3339bced184")
        temperatura = requests.api.get(apiadvisor).json()['data']['temperature']
        clima = requests.api.get(apiadvisor).json()['data']['condition']
        icone_previsao = requests.api.get(apiadvisor).json()['data']['icon']
        cidade = requests.api.get(apiadvisor).json()['name']
    except:
        pass

    return render(request, "index.html", { 'qtd_pedidos': qtd_pedidos,
                                            'qtd_compras': qtd_compras,
                                            'qtd_servicos': qtd_servicos,
                                            'qtd_expedicao': qtd_expedicao,
                                            'data_agora': data_agora,
                                            'temperatura': temperatura,
                                            'clima': clima,
                                            'icone_previsao': icone_previsao,
                                            'cidade': cidade })
