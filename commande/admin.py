from django.contrib import admin
from.models import Commande
@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'produit', 'telephone', 'ville', 'quartier', 'date_commande')
    list_filter = ('date_commande', 'ville')
    search_fields = ('nom', 'telephone', 'produit__nom')
    ordering = ('-date_commande',)
    date_hierarchy = 'date_commande'