from django.shortcuts import render, get_object_or_404
from .models import Categorie, Produit
def accueil(request):
    categories=Categorie.objects.all()
    return render (request, 'boutique/accueil.html',{'categories': categories})

def produits_categorie(request, nom):
    categorie=get_object_or_404(Categorie,nom=nom)
    produits=Produit.objects.filter(categorie=categorie)
    return render(request,'boutique/produits.html',{'categorie':categorie,'produits':produits})

def detail_produit(request, id):
    produit=get_object_or_404(Produit,id=id)
    return render(request,'boutique/detail_produit.html',{'produit':produit})

def a_propos(request):
    return render(request,'boutique/a_propos.html')