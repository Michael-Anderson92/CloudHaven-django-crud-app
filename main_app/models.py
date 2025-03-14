from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('user-detail', kwargs={'pk': self.id})


class Album(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField('User', related_name='albums')
    pictures = models.ManyToManyField('Picture', related_name='albums')
    cover_image = models.ImageField(upload_to='album_covers/', default='album_covers/default.jpg')  

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('album_index')


class Picture(models.Model):
    title = models.CharField(max_length=100)
    comment = models.CharField(max_length=250)
    image = models.ImageField(upload_to='album_pics/', default='album_pics/default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Picture {self.id}"

    def get_absolute_url(self):
        return reverse('picture-detail', kwargs={'pk': self.id})
