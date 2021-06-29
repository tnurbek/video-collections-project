from django.shortcuts import render
from rest_framework import viewsets, generics

from .serializers import CollectionListSerializer, CollectionDetailSerializer, VideoListSerializer, VideoDetailSerializer, ReviewCreateSerializer
from .models import Collection, Video


class CollectionListView(generics.ListAPIView, generics.CreateAPIView):
    """
    collection list view
    """

    def get_queryset(self):
        queryset = Collection.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CollectionListSerializer
        elif self.request.method == 'POST':
            return CollectionDetailSerializer


class CollectionDetailView(generics.RetrieveAPIView):
    """
    collection's full attributes
    """

    serializer_class = CollectionDetailSerializer
    queryset = Collection.objects.all()


class VideoListView(generics.ListCreateAPIView):
    """
    list of videos: not all data shown
    """

    def get_queryset(self):
        queryset = Video.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return VideoListSerializer
        elif self.request.method == 'POST':
            return VideoDetailSerializer


class VideoDetailView(generics.RetrieveAPIView):
    """
    full video display
    """

    serializer_class = VideoDetailSerializer
    queryset = Video.objects.all()


class ReviewCreateView(generics.CreateAPIView):
    """
    review creation view
    """

    serializer_class = ReviewCreateSerializer