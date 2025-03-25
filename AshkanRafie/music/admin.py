from django.contrib import admin
from .models import faq,gallery,SingleTrack
# Register your models here.
admin.site.register(faq)
admin.site.register(gallery)

@admin.register(SingleTrack)
class SingleTrackAdmin(admin.ModelAdmin):
    list_display = ("title", "published_at", "slug", "status")
    list_filter = ("status", "published_at")
    prepopulated_fields = {"slug": ("title",)}
