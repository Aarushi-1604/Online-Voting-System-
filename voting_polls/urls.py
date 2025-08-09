from django.urls import path
from . import views

urlpatterns=[
    path('',views.ongoing_polls,name='ongoing_polls'),
    path('vote/<int:poll_id>/',views.vote,name='vote')
]