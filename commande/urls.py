from django.urls import path
from .import views

urlpatterns=[
    path('commander/<int:produit_id>/', views.commander,name='commander'),
    path('commande/confirmation/<int:commande_id>/', views.confirmation,name='confirmation')

]