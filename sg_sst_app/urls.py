from django.urls import path
from sg_sst_app.views import (
    home,
)

urlpatterns = [
    path("", home, name="home"),
]
