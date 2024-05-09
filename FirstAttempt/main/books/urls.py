from django.urls import path
from . import views

app_name = "books"
urlpatterns = [
    path('add/', views.addBook, name="add"),
    path('', views.index, name="index")
]
