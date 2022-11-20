from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # 유저 관련 기능: 프로필 열람 및 수정, 팔로잉/언팔
    path('profile/<username>/', views.profile),
    path('profile/<username>/follow/', views.follow),
    
]