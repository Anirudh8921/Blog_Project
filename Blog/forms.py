from django import forms
from .models import Blogger, Post

class BloggerForm(forms.ModelForm):
    class Meta:
        model = Blogger
        fields = ['firstname', 'lastname', 'email', 'contact_number']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'imagename', 'content', 'description', 'slug', 'blogger']