from django.urls import path
from.views import event_list, register_event

urlpatterns = [
    path("register/", register_event, name="register_event"),
    path("list/", event_list, name="list"),
]