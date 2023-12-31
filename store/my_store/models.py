from django.db import models


# Create your models here.


class HomeNav(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()


class Products(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


class About(models.Model):
    description = models.TextField()
    image = models.ImageField()


class TestBlog(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()


class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    message = models.TextField()
































