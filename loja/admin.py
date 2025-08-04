from django.contrib import admin
from .models import *

# Register your models here.

class FabricanteAdmin(admin.ModelAdmin):
    # cria um filtro de hierarquia com datas
    date_hierarchy = 'criado_em'
    
class ProdutoAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'
    list_display = ('Produto', 'destaque', 'promocao', 'msgPromocao', 'preco', 'categoria') # formata a tabela de forma diferente
    empty_value_display = 'Vazio' # ficara escrito vazio nos campos que podem ser vazios
    search_fields = ('Produto',) # permite que eu crie um campo de pesquisa em que vai pesquisar utilizando o que está entre aspas


admin.site.register(Fabricante, FabricanteAdmin)
admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Usuario)