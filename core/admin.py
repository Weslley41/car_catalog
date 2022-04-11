from django.contrib import admin

from .models import MarcaCarro, Carro, Vendedor

@admin.register(MarcaCarro)
class MarcaCarroAdmin(admin.ModelAdmin):
	list_display = ('nome',)
	search_fields = ('nome',)


@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
	list_display = ('marca', 'modelo', 'ano', 'destaque')
	search_fields = ('marca__nome', 'modelo', 'ano')


@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
	list_display = ('nome', 'email', 'telefone')
	search_fields = ('nome',)
