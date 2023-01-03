from .  import views
from django.urls import path


urlpatterns = [
    path('', views.getPlan),
    path('Types/', views.getType),
    path('Tasks/', views.getTasks)
]
