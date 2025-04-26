from django.urls import path
from posts import views

urlpatterns = [
    path('home/',views.home),
    path('<int:id>/', views.post, name='post') 
    
]