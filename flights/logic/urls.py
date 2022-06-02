from django.urls import path

from . import views

urlpatterns = [
    path('date_time/', views.PopulateDB)
]
