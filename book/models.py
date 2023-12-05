from django.db import models
from core import models as core_models


class Book(core_models.TimeStampedModel):
    title = models.CharField(max_length=255, default="none", null=False)
    author = models.CharField(max_length=255, default="none", null=False)
    publisher = models.CharField(max_length=255, default="none", null=False)
    publish_date = models.DateTimeField(null=True, blank=True)
    right_price = models.BigIntegerField(null=True, blank=True)
    fake_isbn = models.BigIntegerField(null=True, blank=True)
    url = models.CharField(max_length=1024, default="none", null=False)
    crawl_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


class Metadata(core_models.TimeStampedModel):
    rank = models.BigIntegerField(null=True, blank=True)
    sales_point = models.BigIntegerField(null=True, blank=True)
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    crawl_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.book.title
