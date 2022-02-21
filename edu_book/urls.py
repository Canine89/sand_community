from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        regex=r"^date/$",
        view=views.DatetimeRangeEduBook.as_view(),
    ),
    url(
        regex=r"^datelist/$",
        view=views.DateListEduBook.as_view(),
    ),
    url(
        regex=r"^isbn/$",
        view=views.IsbnEduBook.as_view(),
    ),
]
