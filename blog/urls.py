# urls.py
from django.urls import path
from .views import PostListView, PostCreateView, PostDetailView,ModifierProduit
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('modifier/<int:pk>/', ModifierProduit.as_view(), name='modifier_post'),
    path('supprimer/<int:post_id>/', views.supprimer_post, name='supprimer_post'),


]
