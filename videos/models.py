from django.db import models
from django.contrib.auth.models import User


class Collection(models.Model):
    """
    collections model, group of videos chosen by videos
    """

    title = models.CharField(max_length=255)
    slug = models.SlugField('Slug', max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class Video(models.Model):
    """
    one instance: video
    """

    title = models.CharField(max_length=255)
    url = models.URLField()
    youtube_id = models.CharField(max_length=255)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='videos')

    def __str__(self):
        return f'{self.title.lower()}'


class Review(models.Model):
    """
    review model
    """

    name = models.CharField(max_length=100)
    text = models.TextField()
    parent = models.ForeignKey('self', verbose_name='parent', on_delete=models.SET_NULL, blank=True, null=True,
                               related_name='children')
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='reviews')


    def __str__(self):
        return f'{self.name} - {self.id}'