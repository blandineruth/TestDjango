from django.contrib import admin
from .models import HomeNav
from .models import Website, Testimonial, Contact, SocialNetworks
from .models import Products, About, TestBlog, InstagramFeeds


# Register your models here.


class HomeNavAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'image')


class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description_website', 'email',
                    'contact', 'map')


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'price')


class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'image')


class TestBlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'image')


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'message')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'email', 'message')


class InstagramFeedsAdmin(admin.ModelAdmin):
    list_display = ('id', 'images', 'lien_feeds')


class SocialNetworksAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon', 'lien')


admin.site.register(SocialNetworks, SocialNetworksAdmin)
admin.site.register(InstagramFeeds, InstagramFeedsAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(TestBlog, TestBlogAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Website, WebsiteAdmin)
admin.site.register(HomeNav, HomeNavAdmin)
