from django.urls import path
from.views import course_list, register_courses

urlpatterns = [
    path("register/", register_courses, name="register_courses"),
    path("list/", course_list, name="list"),
]