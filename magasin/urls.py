from django.urls import path
from . import views
from .views import CategoryAPIView
from .views import ProduitAPIView
from rest_framework import routers
from magasin.views import ProductViewset, CategoryAPIView


app_name='magasin'
urlpatterns = [ 
     path('', views.index, name='index'),
     path('list/',views.listProduit,name='liste'),
     path('vitrine/',views.vitrine,name='V'),
      path('nouveauFournisseur/',views.nouveauFournisseur,name='nouveauFour'),
      
      path('register/',views.register, name='register'),
      #path('', views.home,name='home'),
      path('api/category/', CategoryAPIView.as_view()),
      path('api/produits/', ProduitAPIView.as_view()),
      path('api/produit/<int:category_id>', ProduitAPIView.as_view()),

       

]
