from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(regex=r"^$", view=views.ReactAppView.as_view()),
    path("book/", include("book.urls")),
    path("edu_book/", include("edu_book.urls")),
    path("utils/", include("utils.urls")),
]
