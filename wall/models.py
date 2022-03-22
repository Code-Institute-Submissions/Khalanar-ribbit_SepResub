from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Category(models.Model):
    '''ds'''
    name = models.CharField(max_length=12, unique=True)

    class Meta:
        '''ds'''
        verbose_name_plural = "categories"

    def __str__(self):
        return str(self.name)


class Post(models.Model):
    '''Post model'''
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
        '''meta'''
        ordering = ['-date_created']

    def __str__(self):
        '''ds'''
        return str(self.title)

    def number_of_likes(self):
        '''ds'''
        return self.likes.count()


class Comment(models.Model):
    '''ds'''
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        '''ds'''
        ordering = ['date_created']
    
    def __str__(self):
        '''ds'''
        return f"Comment {self.body} by {self.author}"
