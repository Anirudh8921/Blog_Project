from django.db import models

# Create your models here.

class Blogger(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.email} {self.contact_number}"

class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    imagename = models.ImageField(upload_to='images/')
    content = models.TextField()
    description = models.TextField()
    slug = models.SlugField(unique=True)
    blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
