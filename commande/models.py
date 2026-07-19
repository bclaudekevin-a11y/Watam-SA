from django.db import models
from boutique.models import Produit
class Commande(models.Model):
    produit=models.ForeignKey(Produit,on_delete=models.CASCADE)
    nom=models.CharField(max_length=100)
    telephone=models.CharField(max_length=20)
    ville=models.CharField(max_length=50)
    quartier=models.CharField(max_length=50)
    date_commande=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.nom}-{self.produit.nom}"
