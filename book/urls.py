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
        regex=r"^isbn/$",
        view=views.IsbnBook.as_view(),
    ),
]
