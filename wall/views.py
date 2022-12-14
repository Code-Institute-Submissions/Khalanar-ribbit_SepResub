from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Category, Profile
from .forms import CommentForm, PostForm, CategoryForm, ProfileForm
from django.contrib.auth.decorators import login_required
import re


class Home(generic.ListView):
    '''Home view'''
    model = Post
    template_name = 'wall/index.html'
    paginate_by = 25

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
        '''post method to add comment'''
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
            messages.success(request, 'Comment successfully added!')
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


@login_required
def delete_category(request, category):
    """ Delete a category """
    category = get_object_or_404(Category, name=category)
    category.delete()
    messages.success(request, 'Category successfully deleted')
    return redirect(reverse('home'))


@login_required
def delete_post(request, slug):
    """ Delete a post """
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)
    post.delete()
    messages.success(request, 'Post successfully deleted')
    return redirect(reverse('home'))


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
        '''post method to render view'''
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            post_form.instance.author = request.user
            post = post_form.save(commit=False)
            title = post_form.cleaned_data['title']
            post.slug = title.replace(" ", "_").lower()
            post.slug = re.sub(r'\W+', '', post.slug)

            category = post_form.cleaned_data['category']

            messages.success(request, 'Post created!')
            post.save()
        else:
            messages.error(request, 'Invalid form data')
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
            category.name = category.name.replace(" ", "_").lower()
            category.name = re.sub(r'\W+', '', category.name)
            category.save()
        else:
            category_form = CategoryForm()

        messages.success(request, 'New category created!')
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


class EditProfile(LoginRequiredMixin, View):
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

    def post(self, request, *args, **kwargs):
        '''post form data to edit user profile'''
        profile_form = ProfileForm(request.POST, files=request.FILES)
        if profile_form.is_valid():
            if Profile.objects.filter(user=request.user).exists():
                print('USER')
                profile = request.user.profile
            else:
                print('NO USER')
                profile = Profile.create(request.user)

            if profile_form.cleaned_data['name'] != '':
                profile.name = profile_form.cleaned_data['name']
                messages.success(
                    request,
                    f'Name changed to {profile_form.cleaned_data["name"]}'
                )

            if request.FILES.get('profile_picture') is not None:
                profile.profile_picture = request.FILES.get('profile_picture')
                messages.success(request, 'Profile successfully updated')

            profile_pic = request.FILES.get('profile_picture')
            name = profile_form.cleaned_data['name']

            if profile_pic is None and name == '':
                messages.success(request, 'No changes made to your profile')
            else:
                profile.save()

            return redirect('home')


class ComingSoon(View):
    '''Coming soon view'''
    def get(self, request, feature, *args, **kwargs):
        '''get method to render view'''
        return render(request, 'wall/coming_soon.html', {'feature': feature})


def error_500(request, exception):
    return render(request, 'wall/500.html', status=500)


def error_404(request, exception):
    return render(request, 'wall/404.html', status=404)
