from django.shortcuts import render
from core.forms import *
from core.models import *


def list_usuario(request):
    if request.method == 'POST':

        search = request.POST.get('nome_usuario')
        lista_usuario = Usuario.objects.filter(nome__contains=search)

        if search == "":
            search = request.POST.get('email_usuario')
            lista_usuario = Usuario.objects.filter(email__contains=search)

            if search == "":
                search = request.POST.get('cpf_usuario')
                lista_usuario = Usuario.objects.filter(cpf=search)

                if search == "":
                    return render(request, "grupo/grupousuario.html")

        return render(request, "grupo/grupousuario.html", {'lista_usuario':lista_usuario})
    else:
        return render(request, "grupo/grupousuario.html")


def list_cliente(request):
    if request.method == 'POST':
        
        search = request.POST.get('nome_cliente')
        lista_cliente = Cliente.objects.filter(clientename__contains=search)

        if search == "":
            search = request.POST.get('email_cliente')
            lista_cliente = Cliente.objects.filter(email__contains=search)

            if search == "":
                search = request.POST.get('cpf/cnpj_cliente')
                lista_cliente = Cliente.objects.filter(numero_fiscal=search)

                if search == "":
                    return render(request, "grupo/grupocliente.html")

        return render(request, "grupo/grupocliente.html", {'lista_cliente':lista_cliente})
    else:
        return render(request, "grupo/grupocliente.html")
   

def list_fornecedor(request):
    if request.method == 'POST':
        
        search = request.POST.get('nome_fornecedor')
        lista_fornecedor = Fornecedor.objects.filter(fornecedorname__contains=search)

        if search == "":
            search = request.POST.get('email_fornecedor')
            lista_fornecedor = Fornecedor.objects.filter(email__contains=search)

            if search == "":
                search = request.POST.get('cpf/cnpj_fornecedor')
                lista_fornecedor = Fornecedor.objects.filter(numero_fiscal=search)

                if search == "":
                    return render(request, "grupo/grupofornecedor.html")

        return render(request, "grupo/grupofornecedor.html", {'lista_fornecedor':lista_fornecedor})
    else:
        return render(request, "grupo/grupofornecedor.html")


def list_prestador(request):
    if request.method == 'POST':
        
        search = request.POST.get('nome_prestador')
        lista_prestador = PrestadorServico.objects.filter(prestadorname__contains=search)

        if search == "":
            search = request.POST.get('email_prestador')
            lista_prestador = PrestadorServico.objects.filter(email__contains=search)

            if search == "":
                search = request.POST.get('cpf/cnpj_prestador')
                lista_prestador = PrestadorServico.objects.filter(numero_fiscal=search)

                if search == "":
                    return render(request, "grupo/grupoprestador.html")

        return render(request, "grupo/grupoprestador.html", {'lista_prestador':lista_prestador})
    else:
        return render(request, "grupo/grupoprestador.html")


def list_material(request):
    if request.method == 'POST':
        
        search = request.POST.get('cod_material')
        lista_material = Material.objects.filter(cod_mprima=search)

        if search == "":
            search = request.POST.get('tipo_material')
            lista_material = Material.objects.filter(tipo_mprima__contains=search)

            if search == "":
                search = request.POST.get('fabricante')
                lista_material = Material.objects.filter(nome_fabricante__contains=search)

                if search == "":
                    search = request.POST.get('desc_material')
                    lista_material = Material.objects.filter(material__contains=search)

                    if search == "":
                        return render(request, "grupo/grupomaterial.html")

        return render(request, "grupo/grupomaterial.html", {'lista_material':lista_material})
    else:
        return render(request, "grupo/grupomaterial.html")

def list_produto(request):
    return render(request, "grupo/grupoproduto.html")


def list_servico(request):
    return render(request, "grupo/gruposervico.html")


###################################################################################################
def list_registrar_pedido(request):
    if request.method == 'POST':
        
        search = request.POST.get('nome_cliente')
        lista_pedido = Pedido.objects.filter(nome_cliente_contains=search)

        if search == "":
            search = request.POST.get('nome_produto')
            lista_pedido = Pedido.objects.filter(nome_produto_contains=search)

            if search == "":
                search = request.POST.get('nome_tecido')
                lista_pedido = Pedido.objects.filter(nome_tecido_contains=search)

                if search == "":
                    search = request.POST.get('quantidade')
                    lista_pedido= Pedido.objects.filter(quantidade__contains=search)
                    
                    if search == "":
                        search = request.POST.get('tamanho')
                        lista_pedido= Pedido.objects.filter(tamanho__contains=search)

                        if search == "":
                            search = request.POST.get('forma_pagamento')
                            lista_pedido= Pedido.objects.filter(forma_pagamento__contains=search)

                            if search == "":
                                return render(request, "grupo/gruporegistrarpedido.html")

        return render(request, "grupo/gruporegistrarpedido.html", {'lista_registrar_pedido':lista_registrar_pedido})
    else:
        return render(request, "grupo/gruporegistrarpedido.html")

def list_gerenciar_pedido(request):
    if request.method == 'POST':
        
        search = request.POST.get('id_gerenciarpedido')
        lista_gerenciar_pedido = Gerenciar.objects.filter(id_gerenciarpedido_contains=search)

        if search == "":
            search = request.POST.get('status')
            lista_gerenciar_pedido = Gerenciar.objects.filter(status_contains=search)

            if search == "":
                search = request.POST.get('data')
                lista_pedido = Pedido.objects.filter(data_contains=search)

                if search == "":
                    search = request.POST.get('cliente')
                    lista_pedido= Pedido.objects.filter(cliente__contains=search)
                    
                    if search == "":
                        search = request.POST.get('pagamento')
                        lista_pedido= Pedido.objects.filter(pagamento__contains=search)

                        if search == "":
                            search = request.POST.get('total')
                            lista_pedido= Pedido.objects.filter(total__contains=search)

                            if search == "":
                                return render(request, "grupo/grupogerenciarpedido.html")

        return render(request, "grupo/grupogerenciarpedido.html", {'lista_gerenciar_pedido':lista_gerenciar_pedido})
    else:
        return render(request, "grupo/grupogerenciarpedido.html")


def list_ordem_servico(request):
    if request.method == 'POST':
        
        search = request.POST.get('data_servico')
        lista_ordem_servico = Ordem.objects.filter(id_ordemservico_contains=search)

        if search == "":
            search = request.POST.get('id_pedido')
            lista_ordem_servico = Ordem.objects.filter(cliente_contains=search)

            if search == "":
                search = request.POST.get('produto')
                ordem_servico = Ordem.objects.filter(produto_contains=search)

                if search == "":
                    search = request.POST.get('tipo_servico')
                    ordem_servico= Ordem.objects.filter(pagamento__contains=search)
                    
                    if search == "":
                        search = request.POST.get('prestador_servico')
                        ordem_servico= Ordem.objects.filter(transporte__contains=search)

                        if search == "":
                            search = request.POST.get('quantidade')
                            ordem_servico= Ordem.objects.filter(total__contains=search)

                            if search == "":
                                return render(request, "grupo/grupoordemservico.html")

        return render(request, "grupo/grupoordemservico.html", {'lista_ordem_servico':lista_ordem_servico})
    else:
        return render(request, "grupo/grupoordemservico.html")







