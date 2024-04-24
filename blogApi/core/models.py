from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User 


# Create your models here.

class Post(models.Model):
    user = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE )
    title = models.CharField( max_length=50)
    content = models.TextField()
    slug = models.SlugField(unique=True, default='')
    updated = models.DateTimeField( auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField( auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"id": self.id})
        # return '/post/%s/'%{self.id}
    
    