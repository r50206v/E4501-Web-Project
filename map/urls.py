from django.urls import path
from .views import squirrel_map

urlpatterns = [
    path('', squirrel_map)
]