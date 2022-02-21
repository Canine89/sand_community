from django.db import models
from core import models as core_models
from taggit.managers import TaggableManager


# Create your models here.
class EduBook(core_models.TimeStampedModel):
    title = models.CharField(max_length=255, default="none", null=False)
    author = models.CharField(max_length=255, default="none", null=False)
    publisher = models.CharField(max_length=255, default="none", null=False)
    publish_date = models.DateTimeField(null=True, blank=True)
    right_price = models.BigIntegerField(null=True, blank=True)
    sales_price = models.BigIntegerField(null=True, blank=True)
    isbn = models.BigIntegerField(null=True, blank=True)
    url = models.CharField(max_length=1024, default="none", null=False)
    page = models.BigIntegerField(null=True, blank=True)
    tags = TaggableManager()
    crawl_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


class EduMetadata(core_models.TimeStampedModel):
    market = models.CharField(max_length=255, default="none", null=False)
    rank = models.BigIntegerField(null=True, blank=True)
    sales_point = models.BigIntegerField(null=True, blank=True)
    book = models.ForeignKey("EduBook", on_delete=models.CASCADE)
    crawl_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.book.title
