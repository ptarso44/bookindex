from django.urls import path
from .views import views_booklist

urlpatterns = [
    path('', views_booklist.booklist, name='booklist')
]
