from django.urls import path
from guests import views


urlpatterns = [
    path("", views.index, name="index"),   
    
]