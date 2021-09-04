from core.views import home
from django.conf.urls import include
from django.urls.conf import path



urlpatterns = [
path("", home, name="home_page"),
]