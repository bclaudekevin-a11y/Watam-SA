from django.contrib import admin
from .models import Categorie, Produit
admin.site.register(Categorie)


@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'prix_promo', 'est_vedette', 'categorie')
    list_editable = ('est_vedette', 'prix_promo')
    list_filter = ('est_vedette', 'categorie')
