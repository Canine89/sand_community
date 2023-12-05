from django.urls import include, re_path
from . import views


urlpatterns = [
    re_path(r"^$", view=views.ReactAppView.as_view()),
    re_path("book/", include("book.urls")),
]
