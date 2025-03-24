from django.contrib import admin
from .models import Blog

# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "published_at", "slug", "status")
    list_filter = ("status", "published_at")
    prepopulated_fields = {"slug": ("title",)}


