from .models import Comment, Post, Category, Profile
from django import forms
from crispy_forms.helper import FormHelper


class CommentForm(forms.ModelForm):
    '''comment form'''
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['body'].label = ''

    class Meta:
        '''form meta info'''
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    '''Post form'''
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['category'].label = ''
        self.fields['category'].empty_label = None

    class Meta:
        '''form meta info'''
        model = Post
        fields = ('title', 'content', 'category')


class CategoryForm(forms.ModelForm):
    '''Category form'''
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        
    class Meta:
        '''form meta info'''
        model = Category
        fields = ('name',)


class ProfileForm(forms.ModelForm):
    '''Profile form'''
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['name'].initial = ''
        self.fields['name'].required = False

        self.fields['profile_picture'].label = 'Upload new profile picture'
        self.fields['profile_picture'].required = False

    class Meta:
        '''form meta info'''
        model = Profile
        fields = ('name', 'profile_picture', )
