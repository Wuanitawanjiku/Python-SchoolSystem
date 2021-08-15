from django.urls import path
from.views import register_courses

urlpatterns = [
    path("register/", register_courses, name="register_courses"),
]