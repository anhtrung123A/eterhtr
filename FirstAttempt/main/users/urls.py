from django.urls import path
from .import views
app_name = "users"
urlpatterns = [
    path('index/', views.index, name = "index"),
    path('verify/', views.login, name = "login"),
    path('registry/', views.registry, name = "registry")
]