from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers

# from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When


class Book(APIView):
    def get(self, request, format=None):
        yes24_top20_metadatas = models.Metadata.objects.filter(market="yes24")

        serializer = serializers.MetadataSerializer(
            yes24_top20_metadatas,
            many=True,
        )

        return Response(data=serializer.data)
