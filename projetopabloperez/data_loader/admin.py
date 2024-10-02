from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Produto
from django.urls import path
from django.template.response import TemplateResponse
from django.db.models import Count

class CustomAdminSite(AdminSite):
    site_header = 'Admin Pablo Perez'
    site_title = 'Admin Custom'
    index_title = 'Bienvenido al Admin de Pablo Perez'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('dashboard/', self.admin_view(self.dashboard_view), name='dashboard'),
        ]
        return custom_urls + urls

    def dashboard_view(self, request):
        # Obtener todos os produtos
        produtos = Produto.objects.all()
        
        # Obtenha contagem por categoria
        productos_por_categoria = Produto.objects.values('categoria').annotate(total=Count('id'))
        
        context = dict(
            self.each_context(request),
            produtos=produtos,  # Adicione todos os produtos ao contexto
            productos_por_categoria=productos_por_categoria,
        )
        return TemplateResponse(request, "admin/dashboard.html", context)

custom_admin_site = CustomAdminSite(name='custom_admin')

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria', 'preco', 'stock')  
    search_fields = ('nome', 'categoria')
    list_filter = ('categoria', 'stock',)  
    ordering = ('-preco',)

custom_admin_site.register(Produto, ProdutoAdmin)