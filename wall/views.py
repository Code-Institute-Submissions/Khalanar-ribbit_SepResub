from django.shortcuts import render, get_object_or_404
from django.views import generic, View
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

class PostView(View):
    '''ds'''
    def get(self, request, slug, *args, **kwargs):
        '''ds'''
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(post=post).order_by("-date_created")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'wall/post_view.html',
            {
                'post': post,
                'comments': comments,
                'liked': liked,
            },
        )

class CategoryView(View):
    '''ds'''
    def get(self, request, category, *args, **kwargs):
        '''ds'''
        queryset = Category.objects.all()
        category = get_object_or_404(queryset, name=category)
        posts = Post.objects.filter(category=category)

        return render(
            request,
            'wall/category_wall.html',
            {
                'category': category,
                'posts': posts,
            },
        )