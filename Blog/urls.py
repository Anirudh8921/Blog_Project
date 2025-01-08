from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('blogs/', views.all, name='all'),
    path('add-post/', views.add_post, name='add_post'),
    path('add-blog/', views.add_blog, name='add_blog'),
    path('blog/<slug:slug>/', views.detail, name='detail'),
]