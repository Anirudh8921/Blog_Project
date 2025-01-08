from django.shortcuts import render,redirect
from .models import Post
from django.shortcuts import get_object_or_404
from .forms import BloggerForm, PostForm


def add_post(request):
    if request.method == 'POST':
        
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.save()
            return redirect('main')
    else:
       
        post_form = PostForm()
    
    return render(request, 'blog/add_post.html', {
        'post_form': post_form
    })


def add_blog(request):
    if request.method == 'POST':
        blogger_form = BloggerForm(request.POST)
        if blogger_form.is_valid():
            blogger_form.save()
            return redirect('main')  # Redirect to a success page or main page
    else:
        blogger_form = BloggerForm()
    
    return render(request, 'blog/add_blog.html', {
        'blogger_form': blogger_form
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

