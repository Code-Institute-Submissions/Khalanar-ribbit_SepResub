from django.shortcuts import render
from django.views import generic

# Create your views here.
class Home(generic.ListView):
    template_name = 'wall/index.html'
    queryset = 'Post.objects.filter(status=1)'