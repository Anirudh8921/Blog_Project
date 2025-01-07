from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('blogs/', views.all, name='all'),
    path('create-post/', views.create_post, name='create_post'),
    path('blog/<slug:slug>/', views.detail, name='detail'),
]