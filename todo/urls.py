from django.urls import path
from . import views

urlpatterns = [
    path('<int:page>/', views.home, name='home'),
    path('update/<int:id>/', views.update, name='update'),
    path('create/', views.create, name='create'),
]