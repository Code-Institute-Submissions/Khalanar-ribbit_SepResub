from .models import Comment
from django import forms
from crispy_forms.helper import FormHelper


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['body'].label = ''

    class Meta:
        model = Comment
        fields = ('body',)
