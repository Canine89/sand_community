from django.urls import include, re_path
from . import views

urlpatterns = [
    re_path(
        "^$",
        view=views.Book.as_view(),
    ),
    re_path(
        "^date/$",
        view=views.DatetimeRangeBook.as_view(),
    ),
    re_path(
        "^datelist/$",
        view=views.DateListBook.as_view(),
    ),
    re_path(
        "^fakeisbn/$",
        view=views.FakeIsbnBook.as_view(),
    ),
    re_path(
        "^publisher/$",
        view=views.PublisherBook.as_view(),
    ),
    re_path(
        "^yes24/status/$",
        view=views.Yes24Status.as_view(),
    ),
    re_path(
        "^publisher/easyspub/$",
        view=views.EasysBooks.as_view(),
    ),
    re_path(
        "^isbn/$",
        view=views.FullInfoBook.as_view(),
    ),
]
