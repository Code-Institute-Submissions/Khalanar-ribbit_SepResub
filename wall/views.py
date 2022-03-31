from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Category
from .forms import CommentForm, PostForm, CategoryForm, ProfileForm


class Home(generic.ListView):
    '''Home view'''
    model = Post
    template_name = 'wall/index.html'
    paginate_by = 6
    
    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['categories'] = Category.objects.all()
        return context


class PostView(View):
    '''Post view'''
    def get(self, request, slug, *args, **kwargs):
        '''get method to render view'''
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(post=post).order_by("date_created")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'wall/post_view.html',
            {
                'post': post,
                'comments': comments,
                'commented': False,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        '''get method to render view'''
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(post=post).order_by("date_created")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.author = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('post_view', args=[slug]))
        else:
            comment_form = CommentForm()

        return render(
            request,
            'wall/post_view.html',
            {
                'post': post,
                'comments': comments,
                'commented': False,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )


class CategoryView(View):
    '''Category view'''
    def get(self, request, category, *args, **kwargs):
        '''get method to render view'''
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


class NewPostView(View):
    '''New post view'''
    def get(self, request, *args, **kwargs):
        '''get method to render view'''
        return render(
            request,
            'wall/new_post.html',
            {
                'post_form': PostForm(),
            },
        )
    
    def post(self, request, *args, **kwargs):
        '''get method to render view'''
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            post_form.instance.author = request.user
            post = post_form.save(commit=False)
            post.slug = post_form.cleaned_data['title'].replace(" ", "-").lower()
            category = post_form.cleaned_data['category']

            post.save()
            # return HttpResponseRedirect(reverse('post_view')
        else:
            post_form = PostForm()

        return redirect('category_view', category=category)


class NewCategoryView(View):
    '''New Category view'''
    def get(self, request, *args, **kwargs):
        '''get method to render view'''
        return render(
            request,
            'wall/new_category.html',
            {
                'category_form': CategoryForm(),
            },
        )
    
    def post(self, request, *args, **kwargs):
        '''post method to render view'''
        category_form = CategoryForm(data=request.POST)
        if category_form.is_valid():
            category_form.instance.author = request.user
            category = category_form.save(commit=False)
            category.save()
        else:
            category_form = CategoryForm()

        return redirect('category_view', category=category)


class LikePost(View):
    '''Like post view'''
    def post(self, request, slug):
        '''get method to render view'''
        post = get_object_or_404(Post, slug=slug)
        
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        
        return redirect('home')


class EditProfile(View):
    '''Edit Profile view'''
    def get(self, request, *args, **kwargs):
        '''get method to render view'''
        return render(
            request,
            'wall/edit_profile.html',
            {
                'profile_form': ProfileForm(),
            },
        )


class ComingSoon(View):
    '''Coming soon view'''
    def get(self, request, feature, *args, **kwargs):
        '''get method to render view'''
        return render(request, 'wall/coming_soon.html', {'feature': feature})
