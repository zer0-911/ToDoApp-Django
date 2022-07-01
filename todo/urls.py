from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('done/', views.index, name='done'),
    path('pending/', views.index, name='pending'),
    path('delete_all/', views.index, name='delete_all'),
    path('create/', views.index, name='create'),
    path('<int:id>/update/', views.index, name='update'),
    path('<int:id>/delete/', views.index, name='delete'),
]