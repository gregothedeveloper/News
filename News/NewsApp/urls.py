from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='list'),
    path('create/', views.post_create, name='create'),
    path('detail/<int:id>/', views.post_detail, name='detail'),
    path('update/<int:id>/', views.post_update, name='update'),
    path('delete/<int:id>/', views.post_delete, name='delete'),
]
