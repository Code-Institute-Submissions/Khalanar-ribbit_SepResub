from .models import Comment, Post, Category, Profile
from django import forms
from crispy_forms.helper import FormHelper


class CommentForm(forms.ModelForm):
    '''ds'''
    def __init__(self, *args, **kwargs):
        '''ds'''
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['body'].label = ''

    class Meta:
        '''ds'''
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    '''ds'''
    def __init__(self, *args, **kwargs):
        '''ds'''
        super(PostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['category'].label = ''
        self.fields['category'].empty_label = None

    class Meta:
        '''ds'''
        model = Post
        fields = ('title', 'content', 'category')
        # exclude = ['bbb']


class CategoryForm(forms.ModelForm):
    '''ds'''

    def __init__(self, *args, **kwargs):
        '''ds'''
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        
    class Meta:
        '''ds'''
        model = Category
        fields = ('name',)

class ProfileForm(forms.ModelForm):
    '''ds'''

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

    class Meta:
        model = Profile
        fields = ('name', 'profile_picture', )