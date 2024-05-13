from rest_framework.serializers import ModelSerializer
from magasin.models import Categorie
from rest_framework import serializers
from .models import Produit
class CategorySerializer(ModelSerializer):
 class Meta:
  model = Categorie
  fields = ['id', 'name']


class ProduitSerializer(ModelSerializer):
    class Meta:
        model = Produit
        fields = ['id', 'libelle', 'description', 'categorie']

