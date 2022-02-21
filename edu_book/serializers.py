from . import models
from rest_framework import serializers
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer


class EduBookSerializer(serializers.ModelSerializer):

    tags = TagListSerializerField()

    class Meta:
        model = models.EduBook
        fields = "__all__"


class EduMetadataSerializer(serializers.ModelSerializer):

    book = EduBookSerializer()

    class Meta:
        model = models.EduMetadata
        fields = "__all__"
