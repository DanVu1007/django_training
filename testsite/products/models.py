from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=255)        
    slug = models.SlugField(unique=True, max_length=255)
    price = models.SlugField(max_length=255)
    description = models.TextField()
