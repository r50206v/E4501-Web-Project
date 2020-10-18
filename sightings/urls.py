from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.all_squirrels),
    path('add/', views.add),
    path('stats/', views.stats),
    path(r'<unique_squirrel_id>/', views.squirrel_id)
]