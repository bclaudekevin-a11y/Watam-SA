from django.db import models
class Categorie(models.Model):
    nom=models.CharField(max_length=100) 
    image=models.ImageField(upload_to='categories/',blank=True,null=True)
    def __str__(self):
        return self.nom
    
class Produit(models.Model):
    nom=models.CharField(max_length=200)
    description=models.TextField(max_length=200)
    prix=models.PositiveIntegerField(default=0)
    image=models.ImageField(upload_to='produits/', blank=True, null= True)
    categorie=models.ForeignKey(Categorie,on_delete=models.CASCADE, related_name='produits')
    def __str__(self):
        return self.nom