from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView,UpdateView
from django.urls import reverse_lazy
from .models import Post
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from django.views.decorators.http import require_POST


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['title', 'content','author','status','slug','image']
    success_url = reverse_lazy('post_list')

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    

class ModifierProduit(UpdateView):
    model = Post
    template_name = 'modifier.html'
    form_class = PostForm 
    success_url = reverse_lazy('post_list')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Post, pk=pk)

@require_POST
def supprimer_post(request, post_id):
    post= Post.objects.get(id=post_id)
    post.delete()
    return redirect('/blog')