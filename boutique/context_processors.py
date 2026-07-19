from .models import Categorie
def categories_globales(request):
    return{'toutes_categories':Categorie.objects.all()}