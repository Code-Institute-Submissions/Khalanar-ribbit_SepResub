from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Category(models.Model):
    '''Category database model'''
    name = models.CharField(max_length=12, unique=True)

    class Meta:
        '''meta information for model'''
        verbose_name_plural = "categories"

    def __str__(self):
        return str(self.name)


class Post(models.Model):
    '''Post database model'''
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

    class Meta:
        '''meta information for model'''
        ordering = ['-date_created']

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    '''Comment database model'''
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_comments"
    )
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        '''meta information for model'''
        ordering = ['date_created']

    def __str__(self):
        return f"Comment {self.body} by {self.author}"


class Profile(models.Model):
    '''Profile database model'''
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=12, unique=False)
    dark_mode = models.BooleanField()
    profile_picture = CloudinaryField(
        'profile_pic',
        default='static/images/ribbit-logo.png'
    )
    favorite_categories = models.ManyToManyField(
        Category, related_name='favorite_categories',
        blank=True
    )
    saved_posts = models.ManyToManyField(
        Post,
        related_name='favorite_categories',
        blank=True
    )

    def __str__(self):
        return str(self.name)

    @classmethod
    def create(cls, user):
        '''method to create user profiles if one does not exist'''
        profile = cls(user=user, name='', dark_mode=False)
        return profile