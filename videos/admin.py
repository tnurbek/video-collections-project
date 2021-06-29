from django.contrib import admin
from .models import Collection, Video, Review


class VideoInline(admin.TabularInline):
    """
    to add videos instantly after creation of a collection
    """
    model = Video
    extra = 1


class ReviewInline(admin.TabularInline):
    """
    to add a review instantly with video
    """
    model = Review
    extra = 1


class CollectionAdmin(admin.ModelAdmin):
    """
    collection admin
    """
    list_display = ('title', 'user',)
    list_display_links = ('title',)
    search_fields = ('title',)
    inlines = [VideoInline, ]


class VideoAdmin(admin.ModelAdmin):
    """
    video creation
    """
    list_display = ('title', 'collection',)
    list_display_links = ('title',)


class ReviewAdmin(admin.ModelAdmin):
    """
    review creation
    """
    list_display = ('name', 'video')
    list_display_links = ('name',)


admin.site.register(Collection, CollectionAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Review, ReviewAdmin)
