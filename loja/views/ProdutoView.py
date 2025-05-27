from django.shortcuts import render
from loja.models import Produto
from datetime import timedelta, datetime
from django.utils import timezone

def list_produto_view(request, id=None):

    produto = request.GET.get("produto")
    destaque = request.GET.get("destaque")
    promocao = request.GET.get("promocao")
    categoria = request.GET.get("categoria")
    fabricante = request.GET.get("fabricante")
    dias = request.GET.get("dias")

    produtos = Produto.objects.all()
    #print(produtos)

    if dias is not None:
        now = timezone.now()
        now = now - timedelta(days = int(dias)) # Para consultar os produtos cadastrados nos últimos n dias
        produtos = produtos.filter(criado_em__gte=now)
    if destaque is not None:
        produtos = produtos.filter(destaque=destaque)
    if produto is not None:
        produtos = produtos.filter(Produto__contains=produto) # contains permite que a busca seja feita utilizando apenas uma palavra chave, ignorando maiúscula e minúsculas.
    if promocao is not None:
        produtos = produtos.filter(promocao=promocao)
    if categoria is not None:
        produtos = produtos.filter(categoria__Categoria=categoria) # com esse sufixo ele consegue procura pelo nome da categoria.
    if fabricante is not None:
        produtos = produtos.filter(fabricante__Fabricante=fabricante) # com esse sufixo ele consegue procura pelo nome do fabricante.

    if id is not None:
        produtos = produtos.filter(id=id)
    print(produtos)

    context = {
        'produtos': produtos
    }

    return render(request, template_name='produto/produto.html', context=context, status=200)