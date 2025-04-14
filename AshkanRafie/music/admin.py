from django.contrib import admin
from .models import faq,SingleTrack
# Register your models here.
admin.site.register(faq)

@admin.register(SingleTrack)
class SingleTrackAdmin(admin.ModelAdmin):
    list_display = ("title", "published_at", "slug", "status")
    list_filter = ("status", "published_at")
    prepopulated_fields = {"slug": ("title",)}
