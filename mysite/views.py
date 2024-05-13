from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def home(request):
 context={'val':"Menu Acceuil"}
 return render(request,'home.html',context)
