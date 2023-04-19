from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.sample, name="sample"),
    path('get-notes/', views.getNotes, name="get-notes"),
    path('get-note/<str:pk>/', views.getNote, name="get-note"),
    path('update-note/<str:pk>/', views.updateNote, name="update-note"),
    path('delete-note/<str:pk>/', views.deleteNote, name="delete-note"),
    path('create-note/', views.createNote, name="create-note"),
    path('get-name/<str:pm>/', views.getnote, name="get"),
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]