from django.shortcuts import render,redirect, get_object_or_404
from .forms import CommandeForm,Commande
from boutique.models import Produit
def commander(request, produit_id):
    produit= get_object_or_404(Produit, id=produit_id)
    if request.method=='POST':
        form=CommandeForm(request.POST)
        if form.is_valid():
            commande=form.save(commit=False)
            commande.produit=produit
            commande.prix_paye=produit.prix
            commande.save()
            return redirect('confirmation',commande_id=commande.id)
    else:
        form=CommandeForm()
    return render(request,'commande/formulaire.html',{'form':form,'produit':produit})

def confirmation(request,commande_id):
     commande=get_object_or_404(Commande,id=commande_id)
     return render(request,'commande/confirmation.html',{'commande':commande})