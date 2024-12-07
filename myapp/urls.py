from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('increment/', views.increment_counter, name='increment'),
]
