from django.contrib import admin
from .models import HomeNav
from .models import Contact
from .models import Products, About, TestBlog


# Register your models here.

class HomeNavAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'image')


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'price')


class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'image')


class TestBlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'image')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'email', 'message')


admin.site.register(Contact, ContactAdmin)
admin.site.register(TestBlog, TestBlogAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(HomeNav, HomeNavAdmin)
