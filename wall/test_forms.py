from django.test import TestCase
from .forms import CommentForm, CategoryForm, PostForm, ProfileForm


class TestCommentForm(TestCase):
    '''Test class for CommentForm'''
    def test_comment_body_is_required(self):
        '''ds'''
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_meta(self):
        '''ds'''
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ('body', ))


class TestPostForm(TestCase):
    '''Test class for PostForm'''
    def test_post_has_body(self):
        '''test if post body is required'''
        form = PostForm({'body': '', })
        self.assertFalse(form.is_valid())

    def test_post_has_category(self):
        '''test if post category is required'''
        form = PostForm({'category': '', })
        self.assertFalse(form.is_valid())


class TestCategoryForm(TestCase):
    '''Test class for CategoryForm'''
    def test_category_name_is_required(self):
        '''test if the category name is required'''
        form = CategoryForm({'name': ''})
        self.assertFalse(form.is_valid())


class TestProfileForm(TestCase):
    '''Test class for user profile edits both
        fields can be empty, no need to test required
        '''
    def test_profile_fields_are_explicit_in_meta(self):
        '''Test if only profile fields explicited through Meta
        are available in the form'''
        form = ProfileForm()
        self.assertEqual(form.Meta.fields, ('name', 'profile_picture'))
