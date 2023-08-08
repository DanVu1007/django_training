from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length=255)    
    slug = models.SlugField(unique=True, max_length=255)
    image_url = models.TextField()

class Product(models.Model):
    name = models.CharField(max_length=255)        
    slug = models.SlugField(unique=True, max_length=255)
    price = models.SlugField(max_length=255)
    description = models.TextField()

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)