from rest_framework import serializers
from .models import Collection, Video, Review


class FilterReviewSerializer(serializers.ListSerializer):
    """filter to show only parents"""

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """recursive serializer"""

    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(instance, context=self.context)
        return serializer.data


class VideoListSerializer(serializers.ModelSerializer):
    """
    video list serializer
    """

    # collection = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Video
        fields = ('id', 'title',)


class ReviewSerializer(serializers.ModelSerializer):
    """
    review serializer to show hierarchy
    """

    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterReviewSerializer
        model = Review
        fields = ('name', 'text', 'children')


class VideoDetailSerializer(serializers.ModelSerializer):
    """
    video detail serializer
    """

    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Video
        fields = '__all__'


class CollectionListSerializer(serializers.HyperlinkedModelSerializer):
    """
    video collection serializer
    """

    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Collection
        fields = ('url', 'title', 'user')
        # fields = '__all__'


class CollectionDetailSerializer(serializers.ModelSerializer):
    """
    collection detail
    """

    videos = VideoListSerializer(many=True, read_only=True)

    class Meta:
        model = Collection
        fields = '__all__'


class ReviewCreateSerializer(serializers.ModelSerializer):
    """
    review create [post] serializer
    """

    class Meta:
        model = Review
        fields = '__all__'
