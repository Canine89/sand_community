from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers
from datetime import datetime
from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When
from itertools import chain


class Book(APIView):
    def get(self, request, format=None):
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


class CompareBook(APIView):
    def get(self, request, format=None):
        publisher = "이지스퍼블리싱"
        year = 2021
        month = 8
        day = 25

        metadatas = models.Metadata.objects.values("book__isbn")
        print(metadatas)

        serializer = serializers.MetadataSerializer(metadatas, many=True)

        return Response(data=serializer.data)


class PublisherBook(APIView):
    def get(self, request, format=None):
        publisher = request.query_params.get("publisher", None)
        year = request.query_params.get("year", None)
        month = request.query_params.get("month", None)
        day = request.query_params.get("day", None)
        result = []

        print(publisher, year, month, day)

        metadata_1 = models.Metadata.objects.filter(book__isbn=9791163032748)
        metadata_2 = models.Metadata.objects.filter(book__isbn=9791197149801)
        metadatas = metadata_1.union(metadata_2)

        print(metadatas)

        # metadatas = models.Metadata.objects.filter(
        #     market="yes24",
        #     crawl_date__year=year,
        #     crawl_date__month=month,
        #     crawl_date__day=day,
        #     book__publisher=publisher,
        # )
        #
        # for metadata in metadatas:
        #     _isbn = metadata.book.isbn
        #     _metadatas = models.Metadata.objects.filter(book__isbn=_isbn).order_by(
        #         "crawl_date"
        #     )
        #     print(_metadatas)
        #     result.append(_metadatas)

        serializer = serializers.MetadataSerializer(metadatas, many=True)

        return Response(data=serializer.data)
