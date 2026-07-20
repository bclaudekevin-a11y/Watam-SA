from django.shortcuts import render, get_object_or_404
from .models import Categorie, Produit
def accueil(request):
    categories = Categorie.objects.all()
    # On récupère uniquement les produits cochés "est_vedette"
    produits_vedettes = Produit.objects.filter(est_vedette=True) 
    
    context = {
        'categories': categories,
        'produits_vedettes': produits_vedettes,
    }
    return render(request, 'boutique/accueil.html', context)

def produits_categorie(request, nom):
    categorie=get_object_or_404(Categorie,nom=nom)
    produits=Produit.objects.filter(categorie=categorie)
    return render(request,'boutique/produits.html',{'categorie':categorie,'produits':produits})

def detail_produit(request, id):
    produit=get_object_or_404(Produit,id=id)
    return render(request,'boutique/detail_produit.html',{'produit':produit})

def a_propos(request):
    return render(request,'boutique/a_propos.html')

def recherche(request):
    requete = request.GET.get('q', '')
    resultats = []
    if requete:
        resultats = Produit.objects.filter(nom__icontains=requete)
    return render(request, 'boutique/resultats_recherche.html', {
        'resultats': resultats,
        'requete': requete,
    })