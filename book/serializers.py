from . import models
from rest_framework import serializers
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer


class BookSerializer(serializers.ModelSerializer):

    tags = TagListSerializerField()

    class Meta:
        model = models.Book
        fields = "__all__"


class MetadataSerializer(serializers.ModelSerializer):

    book = BookSerializer()

    class Meta:
        model = models.Metadata
        fields = "__all__"
