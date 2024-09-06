from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListView.as_view(), name='list'),
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='delete'),
]
