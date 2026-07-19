from django.urls import path
from .import views
urlpatterns=[
    path('',views.accueil,name='accueil'),
    path('categorie/<str:nom>/',views.produits_categorie, name='produits_categorie'),
    path('produit/<int:id>/',views.detail_produit, name='detail_produit'),
    path('a_propos/',views.a_propos,name='a_propos')
]