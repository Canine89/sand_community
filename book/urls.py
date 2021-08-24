from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        regex=r"$",
        view=views.Book.as_view(),
    ),
]
