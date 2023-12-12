from django.contrib import admin
from .models import SocialNetworks, InstagramFeeds, Testimonial, Website

# Register your models here.


class InstagramFeedsAdmin(admin.ModelAdmin):
    list_display = ('id', 'images', 'lien_feeds')


class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description_website', 'email',
                    'contact', 'map')


class SocialNetworksAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon', 'lien')


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'message')


admin.site.register(SocialNetworks, SocialNetworksAdmin)
admin.site.register(InstagramFeeds, InstagramFeedsAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Website, WebsiteAdmin)
