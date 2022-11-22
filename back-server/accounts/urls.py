from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token

app_name = 'accounts'

urlpatterns = [
    # 유저 관련 기능: 프로필 열람 및 수정, 팔로잉/언팔
    path('profile/<str:username>/', views.profile_or_edit),
    path('profile/<str:username>/follow/', views.follow),
    
]