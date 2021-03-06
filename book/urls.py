from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        regex=r"^$",
        view=views.Book.as_view(),
    ),
    url(
        regex=r"^date/$",
        view=views.DatetimeRangeBook.as_view(),
    ),
    url(
        regex=r"^datelist/$",
        view=views.DateListBook.as_view(),
    ),
    url(
        regex=r"^isbn/$",
        view=views.IsbnBook.as_view(),
    ),
    url(
        regex=r"^publisher/$",
        view=views.PublisherBook.as_view(),
    ),
    url(
        regex=r"^publisher/status/$",
        view=views.PublisherStatus.as_view(),
    ),
    url(
        regex=r"^count/tags/$",
        view=views.CountTags.as_view(),
    ),
    url(
        regex=r"^publisher/easyspub/$",
        view=views.EasysBooks.as_view(),
    ),
]
