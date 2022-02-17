from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        regex=r"^transpdf/$",
        view=views.TransformPdf.as_view(),
    ),
]