from django.urls import path

from . import views

urlpatterns = [
    path('some_path/', views.some_function),
    path('price/<str:currency>/', views.price),
    path('price/<str:currency>/<str:base>/', views.price),
]