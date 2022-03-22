from django.shortcuts import render
from django.views import generic
from .models import Post, Category

# Create your views here.
class Home(generic.ListView):
    '''ds'''
    model = Post
    template_name = 'wall/index.html'
    # queryset = 'Post.objects.filter(status=1)'
    # queryset = Post.objects.all()
    paginate_by = 6
    
    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['categories'] = Category.objects.all()
        return context