import re
import os
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
        ).order_by("rank")

        serializer = serializers.MetadataSerializer(
            metadatas,
            many=True,
        )

        return Response(data=serializer.data)


class DateListBook(APIView):
    folderName = "./datas/yes24_json_dump/"

    def get(self, request, format=None):
        datelist = []
        for _file in os.listdir(self.folderName):
            if _file == ".DS_Store":
                continue

            datelist.append(_file[6:15])

        return Response(datelist)


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


class PublisherBook(APIView):
    def get(self, request, format=None):
        publisher = request.query_params.get("publisher", None)

        metadatas = models.Metadata.objects.select_related("book").filter(
            market="yes24",
            book__publisher=publisher,
        )

        serializer = serializers.MetadataSerializer(metadatas, many=True)

        return Response(data=serializer.data)


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
                sales_point_avg=Avg("sales_point"),
                rank_avg=Avg("rank"),
                number_of_book=Count("book__title"),
            )
            .order_by("-sales_point_sum")
        )

        return Response(result)


class CountTags(APIView):
    def get(self, request, format=None):
        totalTags = {}
        for book in models.Book.objects.all():
            tidyTagsPart = list(set(" ".join(list(book.tags.names())).replace("#", "").split(" ")))
            
            try:
                tidyTagsPart.remove("모바일")
            except:
                pass
            
            try:
                tidyTagsPart.remove("IT")
            except:
                pass
            
            try:
                tidyTagsPart.remove("국내도서")
            except:
                pass
            
            try:
                tidyTagsPart.remove("컴퓨터")
            except:
                pass
            
            try:
                tidyTagsPart.remove("프로그래밍")
            except:
                pass
            
            try:
                tidyTagsPart.remove("컴공")
            except:
                pass
            
            try:
                tidyTagsPart.remove("공학")
            except:
                pass
            
            for item in tidyTagsPart:
                try: 
                    totalTags[item] = totalTags[item] + 1
                except:
                    totalTags[item] = 1

        temp = dict(sorted(totalTags.items(), key=lambda x: x[1], reverse=True)[0:100])
        result = []
        for key, value in temp.items():
            result.append({"tagName": key, "tagCount": value})

        return Response(result)