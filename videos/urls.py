from django.urls import path
from . import views

urlpatterns = [
    path('collections/', views.CollectionListView.as_view()),  # list [get]
    path('collections/<int:pk>/', views.CollectionDetailView.as_view(), name='collection-detail'),  # retrieve [get]
    path('videos/', views.VideoListView.as_view()),  # list [get]
    path('videos/<int:pk>/', views.VideoDetailView.as_view()),  # retrieve [get]
    path('reviews/', views.ReviewCreateView.as_view()),  # create [post]
]
