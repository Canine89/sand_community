import re
import os
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers
from datetime import datetime
from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When
from itertools import chain
from collections import Counter


class DateListEduBook(APIView):
    folderName = "./datas/edu_yes24_json_dump/"

    def get(self, request, format=None):
        datelist = []
        for _file in os.listdir(self.folderName):
            if _file == ".DS_Store":
                continue

            datelist.append(_file[6:15])
        return Response(sorted(datelist, reverse=True))


class DatetimeRangeEduBook(APIView):
    def get(self, request, format=None):
        year = request.query_params.get("year", None)
        month = request.query_params.get("month", None)
        day = request.query_params.get("day", None)
        category = request.query_params.get("category", None)

        metadatas = models.EduMetadata.objects.filter(
            book__category=category,
            market="yes24",
            crawl_date__year=year,
            crawl_date__month=month,
            crawl_date__day=day,
        )

        serializer = serializers.EduMetadataSerializer(
            metadatas,
            many=True,
        )

        return Response(data=serializer.data)


class IsbnEduBook(APIView):
    def get(self, request, format=None):
        isbn = request.query_params.get("id", None)
        category = request.query_params.get("category", None)

        metadatas = models.EduMetadata.objects.filter(Q(book__isbn=isbn, book__category=category)).order_by(
            "crawl_date"
        )

        serializer = serializers.EduMetadataSerializer(
            metadatas,
            many=True,
        )

        return Response(data=serializer.data)
