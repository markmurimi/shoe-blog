from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Post, Profile


class PostForm(forms.ModelForm):
    '''
    Class to create a form for an authenticated user to create Post
    '''
    class Meta:
        model = Post
        fields = ['name','picture', 'brand','price', 'post_caption', 'released']