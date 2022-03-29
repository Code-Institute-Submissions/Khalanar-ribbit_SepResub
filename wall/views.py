from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Category
from .forms import CommentForm, PostForm, CategoryForm, ProfileForm


class Home(generic.ListView):
    '''ds'''
    model = Post
    template_name = 'wall/index.html'
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
        '''ds'''
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


class NewPostView(View):
    '''ds'''
    def get(self, request, *args, **kwargs):
            '''ds'''
            return render(
                request,
                'wall/new_post.html',
                {
                    'post_form': PostForm(),
                },
            )
    
    def post(self, request, *args, **kwargs):
        '''ds'''
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
    '''ds'''
    def get(self, request, *args, **kwargs):
            '''ds'''
            return render(
                request,
                'wall/new_category.html',
                {
                    'category_form': CategoryForm(),
                },
            )
    
    def post(self, request, *args, **kwargs):
        '''ds'''
        category_form = CategoryForm(data=request.POST)
        if category_form.is_valid():
            category_form.instance.author = request.user
            category = category_form.save(commit=False)
 

            category.save()
            # return HttpResponseRedirect(reverse('post_view')
        else:
            category_form = CategoryForm()

        return redirect('category_view', category=category)

class LikePost(View):
    '''ds'''
    def post(self, request, slug):
        '''ds'''
        post = get_object_or_404(Post, slug=slug)
        
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        
        return redirect('home')

class EditProfile(View):
    '''ds'''
    def get(self, request, *args, **kwargs):
        '''ds'''
        return render(
            request,
            'wall/edit_profile.html',
            {
                'profile_form': ProfileForm(),
            },
        )