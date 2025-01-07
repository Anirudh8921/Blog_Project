from django.shortcuts import render,redirect
from .models import Post
from django.shortcuts import get_object_or_404
from .forms import BloggerForm, PostForm


def create_post(request):
    if request.method == 'POST':
        blogger_form = BloggerForm(request.POST)
        post_form = PostForm(request.POST, request.FILES)
        if blogger_form.is_valid() and post_form.is_valid():
            blogger = blogger_form.save()
            post = post_form.save(commit=False)
            post.blogger = blogger
            post.save()
            return redirect('homepage')
    else:
        blogger_form = BloggerForm()
        post_form = PostForm()
    
    return render(request, 'blog/create_post.html', {
        'blogger_form': blogger_form,
        'post_form': post_form
    })


def main(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    return render(request, 'blog/main.html', {'posts': latest_posts})

def all(request):
    posts = Post.objects.all()
    return render(request, 'blog/all.html', {'posts': posts})


def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/detail.html', {'post': post})

from django.shortcuts import render, redirect
from .forms import BloggerForm, PostForm
