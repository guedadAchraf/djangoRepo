
from django.contrib import admin
from django.urls import path,include
from .views import home
from .views import HelloAchrafView


urlpatterns = [

    path('', home),
    path('hello/', HelloAchrafView.as_view(), name='hello-achraf'),

]
