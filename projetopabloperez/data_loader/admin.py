from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Produto
from django.urls import path
from django.template.response import TemplateResponse
from django.db.models import Count

# Definindo um AdminSite personalizado
class CustomAdminSite(AdminSite):
    site_header = 'Admin Pablo Perez'
    site_title = 'Admin Custom'
    index_title = 'Vem vindo ao Admin de Pablo Perez'

    # URLs personalizadas
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('dashboard/', self.admin_view(self.dashboard_view), name='dashboard'),
        ]
        return custom_urls + urls

    # visualização do painel
    def dashboard_view(self, request):
        productos_por_categoria = Produto.objects.values('categoria').annotate(total=Count('id'))
        context = dict(
            self.each_context(request),
            productos_por_categoria=productos_por_categoria,
        )
        return TemplateResponse(request, "admin/dashboard.html", context)

# Inicialize o AdminSite personalizado
custom_admin_site = CustomAdminSite(name='custom_admin')

# Registre o modelo do Produto no Admin personalizado
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria', 'preco', 'stock')  
    search_fields = ('nome', 'categoria')
    list_filter = ('categoria', 'stock',)  
    ordering = ('-preco',)

# Cadastre o modelo e o administrador
custom_admin_site.register(Produto, ProdutoAdmin)
