from django.shortcuts import render, redirect
from core.forms import *
from core.models import *


def delete_usuario(request, id):
    delete_usuario = Usuario.objects.get(id=id)

    if request.method == 'POST':
        delete_usuario.delete()
        return redirect('list_usuario')
    
    return render(request, "exclusaoConf.html", {'delete_usuario': delete_usuario})


def delete_cliente(request, id):
    delete_cliente = Cliente.objects.get(id=id)

    if request.method == 'POST':
        delete_cliente.delete()
        return redirect('list_cliente')
    
    return render(request, "exclusaoConf.html", {'delete_cliente': delete_cliente})


def delete_fornecedor(request, id):
    delete_fornecedor = Fornecedor.objects.get(id=id)

    if request.method == 'POST':
        delete_fornecedor.delete()
        return redirect('list_fornecedor')
    
    return render(request, "exclusaoConf.html", {'delete_fornecedor': delete_fornecedor})


def delete_prestador(request, id):
    delete_prestador = PrestadorServico.objects.get(id=id)

    if request.method == 'POST':
        delete_prestador.delete()
        return redirect('list_prestador')
    
    return render(request, "exclusaoConf.html", {'delete_prestador': delete_prestador})


def delete_material(request, id):
    delete_material = Material.objects.get(id=id)

    if request.method == 'POST':
        delete_material.delete()
        return redirect('list_material')
    
    return render(request, "exclusaoConf.html", {'delete_material': delete_material})


def delete_produto(request, id):
    delete_produto = Produto.objects.get(id=id)

    if request.method == 'POST':
        delete_produto.delete()
        return redirect('list_produto')
    
    return render(request, "exclusaoConf.html", {'delete_produto': delete_produto})

    


def delete_servico(request, id):
    delete_servico = Servico.objects.get(id=id)

    if request.method == 'POST':
        delete_servico.delete()
        return redirect('list_servico')
    
    return render(request, "exclusaoConf.html", {'delete_servico': delete_servico})
##############################################################################################

def delete_registrar_pedido(request, id):
    delete_registrar_pedido = Pedido.objects.get(id=id)

    if request.method == 'POST':
        delete_registrar_pedido.delete()
        return redirect('list_registrar_pedido')
    
    return render(request, "exclusaoConf.html", {'delete_registrar_pedido': delete_registrar_pedido})

def delete_gerenciar_pedido(request, id):
    delete_gerenciar_pedido = Gerenciar.objects.get(id=id)

    if request.method == 'POST':
        delete_gerenciar_pedido.delete()
        return redirect('list_gerenciar_pedido')
    
    return render(request, "exclusaoConf.html", {'delete_gerenciar_pedido': delete_gerenciar_pedido})

def delete_ordem_servico(request, id):
    delete_ordem_servico = Ordem.objects.get(id=id)

    if request.method == 'POST':
        delete_ordem_servico.delete()
        return redirect('list_ordem_servico')
    
    return render(request, "exclusaoConf.html", {'delete_ordem_servico': delete_ordem_servico})