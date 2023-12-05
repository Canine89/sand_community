from . import models
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = "__all__"


class MetadataSerializer(serializers.ModelSerializer):

    book = BookSerializer()

    class Meta:
        model = models.Metadata
        fields = "__all__"
