from django.db import models

# Create your models here.


class Website(models.Model):
    name = models.CharField(max_length=255)
    description_website = models.TextField()
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=255)
    map = models.TextField()


class InstagramFeeds(models.Model):
    images = models.ImageField()
    lien_feeds = models.URLField()


class SocialNetworks(models.Model):
    name = models.CharField(max_length=255)
    icon = models.FileField()  
    lien = models.URLField()


class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField()
