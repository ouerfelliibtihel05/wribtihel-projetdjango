from django.template import loader
from .models import Produit
from .models import Fournisseur
from .forms import ProduitForm
from .forms import  FournisseurForm
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate,  logout
from django.contrib import messages
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from magasin.models import Categorie
from magasin.serializers import CategorySerializer
from rest_framework import generics
from .models import Produit
from .serializers import ProduitSerializer
from rest_framework import viewsets






def produit(request):
   # template=loader.get_template('magasin/mesProduits.html')
    products= Produit.objects.all()
    context={'products':products}
    return render( request,'magasin/mesProduits.html',context )
 

def listProduit(request):
    if request.method == "POST":
        forms = ProduitForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            
            return HttpResponseRedirect('/magasin')
    else:
        form = ProduitForm()  # créer formulaire vide
    return render(request, 'magasin/majProduits.html', {'form': form})

def vitrine(request):
    list=Produit.objects.all()
    return render(request,'magasin/vitrine.html',{'list':list})

def index(request):
    return render(request,'magasin/acceuil.html' )

def nouveauFournisseur(request):
    if request.method == "POST":
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin')
    else:
        form = FournisseurForm()
        fournisseurs=Fournisseur.objects.all()
    return render(request, 'magasin/fournisseur.html', {'form': form,'fournisseurs':fournisseurs})



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def my_view(request):
 return redirect('/blog')

class CategoryAPIView(APIView):
 def get(self, *args, **kwargs):
  categories = Categorie.objects.all()
  serializer = CategorySerializer(categories, many=True)
  return Response(serializer.data)


class ProduitAPIView(generics.ListAPIView):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer
    
class ProductViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProduitSerializer
    def get_queryset(self):
        queryset = Produit.objects.all()
        category_id = self.request.GET.get('category_id')
        if category_id:
            queryset = queryset.filter(categorie_id=category_id)
        return queryset
    