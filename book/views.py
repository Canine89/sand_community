import re
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers
from datetime import datetime
from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When
from itertools import chain


class Book(APIView):
    def get(self, format=None):
        _datetime = datetime.now()
        metadatas = models.Metadata.objects.filter(
            market="yes24",
            crawl_date__year=_datetime.year,
            crawl_date__month=_datetime.month,
            crawl_date__day=_datetime.day,
        )

        serializer = serializers.MetadataSerializer(
            metadatas,
            many=True,
        )

        return Response(data=serializer.data)


class DatetimeRangeBook(APIView):
    def get(self, request, format=None):
        year = request.query_params.get("year", None)
        month = request.query_params.get("month", None)
        day = request.query_params.get("day", None)

        metadatas = models.Metadata.objects.filter(
            market="yes24",
            crawl_date__year=year,
            crawl_date__month=month,
            crawl_date__day=day,
        )

        serializer = serializers.MetadataSerializer(
            metadatas,
            many=True,
        )

        return Response(data=serializer.data)


class IsbnBook(APIView):
    def get(self, request, format=None):
        isbn = request.query_params.get("id", None)

        metadatas = models.Metadata.objects.filter(Q(book__isbn=isbn)).order_by(
            "crawl_date"
        )

        serializer = serializers.MetadataSerializer(
            metadatas,
            many=True,
        )

        return Response(data=serializer.data)


"""
    PublisherBook not ended...
"""


class PublisherBook(APIView):
    def get(self, request, format=None):
        publisher = request.query_params.get("publisher", None)

        metadatas = models.Metadata.objects.select_related("book").filter(
            market="yes24",
            book__publisher=publisher,
        )

        serializer = serializers.MetadataSerializer(metadatas, many=True)

        return Response(data=serializer.data)


# class PublisherStatus(APIView):
#     def get(self, request, format=None):
#         publisher = request.query_params.get("publisher", None)
#         year = request.query_params.get("year", None)
#         month = request.query_params.get("month", None)
#         day = request.query_params.get("day", None)

#         sales_point_sum = models.Metadata.objects.filter(book__publisher__icontains=publisher).aggregate(Sum('sales_point'))["sales_point__sum"]
#         sales_point_avg = models.Metadata.objects.filter(book__publisher__icontains=publisher).aggregate(Avg('sales_point'))["sales_point__avg"]
#         count = models.Metadata.objects.filter(
#             book__publisher__icontains=publisher,
#             crawl_date__year=year,
#             crawl_date__month=month,
#             crawl_date__day=day,
#         ).count()

#         result = {"count": count, "sales_point_sum": sales_point_sum, "sales_point_avg": sales_point_avg}
#         print(result)

#         return Response(result)


class PublisherStatus(APIView):
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
                sales_point_avg=round(Avg("sales_point"), 2),
                rank_avg=round(Avg("rank"), 2),
                number_of_book=Count("book__title")
            )
            .order_by("-sales_point_sum")
        )

        return Response(result)
