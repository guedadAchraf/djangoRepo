from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('api/', include('myapp.urls')),  # Ensure 'myapp' is the name of your app
]
