from django.urls import include, re_path
from . import views

urlpatterns = [
    re_path(
        "^$",
        view=views.FakeIsbnBooks.as_view(),
    ),
    re_path(
        "^daterange/$",
        view=views.DateRangeBooks.as_view(),
    ),
    re_path(
        "^datelist/$",
        view=views.DateList.as_view(),
    ),
    re_path(
        "^yes24/status/$",
        view=views.Yes24Status.as_view(),
    ),
]
