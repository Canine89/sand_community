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


class DateList(APIView):
    folderName = "./yes24/linting_dump_datas"

    def get(self, request, format=None):
        datelist = []
        for _file in os.listdir(self.folderName):
            if _file == ".DS_Store":
                continue

            datelist.append(_file[6:15])
        return Response(sorted(datelist, reverse=True))


class DateRangeBooks(APIView):
    def get(self, request, format=None):
        year = request.query_params.get("year", None)
        month = request.query_params.get("month", None)
        day = request.query_params.get("day", None)

        metadatas = models.Metadata.objects.filter(
            crawl_date__year=year,
            crawl_date__month=month,
            crawl_date__day=day,
        )

        serializer = serializers.MetadataSerializer(
            metadatas,
            many=True,
        )

        return Response(data=serializer.data)


class FakeIsbnBooks(APIView):
    def get(self, request, format=None):
        fisbn = request.query_params.get("fisbn", None)

        metadatas = models.Metadata.objects.filter(Q(book__fake_isbn=fisbn)).order_by(
            "crawl_date"
        )

        print(metadatas)

        serializer = serializers.MetadataSerializer(
            metadatas,
            many=True,
        )

        return Response(data=serializer.data)


class Yes24Status(APIView):
    def get(self, request, format=None):
        year = request.query_params.get("year", None)
        month = request.query_params.get("month", None)
        day = request.query_params.get("day", None)

        result = (
            models.Metadata.objects.filter(
                crawl_date__year=year, crawl_date__month=month, crawl_date__day=day
            )
            .values("book__publisher")
            .annotate(
                sales_point_sum=Sum("sales_point"),
                sales_point_avg=Avg("sales_point"),
                rank_avg=Avg("rank"),
                number_of_book=Count("book__title"),
            )
            .order_by("-sales_point_sum")
        )

        return Response(result)
