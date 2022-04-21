from django.urls import path
from To_Do_List_App.views import home

urlpatterns = [
    path('', home),
]