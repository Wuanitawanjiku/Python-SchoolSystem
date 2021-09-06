# from .models import Events
# from django.urls import path
# from.views import event_list, register_event
from django.conf.urls import url
from .import views
app_name = 'cal'

urlpatterns = [  
    url(r'^index/$', views.index, name='index'),
    url(r'^cal/$', views.CalendarView.as_view(), name='calendar'),
    url(r'^event/new/$', views.event, name='event_new'),
	url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),  
]