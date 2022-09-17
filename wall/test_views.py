from django.test import TestCase, Client
from .models import Category, Post, User, Comment


class TestViews(TestCase):
    '''Class to test project views'''
    def test_homepage(self):
        '''test if homepage loads'''
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('wall/index.html')

    def test_new_categories(self):
        '''test if categories can be created and saved'''
        response = self.client.post('/new_category', {'name': 'python'})
        self.assertRedirects(response, '/r/python')

    def test_category_wall(self):
        '''test if category pages can be viewed'''
        category = Category.objects.create(name='python')
        response = self.client.get(f'/r/{category.name}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('wall/category_wall.html')

    def test_new_post_view(self):
        '''test if new post loads'''
        category = Category.objects.create(name='python')
        user = User.objects.create(username='admin')
        post = Post.objects.create(
            content='abc',
            slug='abc',
            category=category,
            author=user
        )
        response = self.client.post('/new_post', {
            'post': post,
            'category': category,
            })
        self.assertRedirects(response, '/r/default')

    def test_post_view(self):
        '''test if posts can be viewed'''
        category = Category.objects.create(name='python')
        user = User.objects.create(username='admin')
        post = Post.objects.create(
            content='abc',
            slug='abc',
            category=category,
            author=user
        )
        response = self.client.get(f'/p/{post.slug}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('wall/post_view.html')
        self.assertTrue(post.likes.count() >= 0)

    def test_commingsoon(self):
        '''test if comingsoon page loads'''
        response = self.client.get('/coming_soon/test')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('wall/comint_soon.html')

    def test_edit_profile(self):
        '''test if settings load'''
        user = User.objects.create(username='admin')
        user.set_password('12345')
        user.save()
        c = Client()
        logged_in = c.login(username='admin', password='12345')

        response = self.client.post(
            '/edit_profile',
            {'username': 'newname', 'profile_picture': 'abc.jpg'}
        )
        self.assertRedirects(response, '/accounts/login/?next=/edit_profile')

    def test_load_profile(self):
        '''test if settings load'''
        response = self.client.get('/edit_profile', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('wall/edit_profile.html')
