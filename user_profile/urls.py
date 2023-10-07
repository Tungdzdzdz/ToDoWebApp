from django.urls import path

from user_profile import views

urlpatterns = [
    path('', views.my_profile, name='profile'),
    path('update/', views.update_profile, name='profile-update'),
]