from rest_framework_jwt.views import obtain_jwt_token
from accounts.views import UserAPIView
from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    # 유저 관련 기능: 프로필 열람 및 수정, 팔로잉/언팔
    # path('signup/', views.signup, name='signup'),
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
    path('', UserAPIView.as_view(), name='user'),
    path('api-token-auth/', obtain_jwt_token),
    path('rest-auth/', include("rest_auth.urls")),
    path('profile/<int:user_id>', views.profile, name='profile'),
    path('profile/<int:user_id>/follow/', views.follow, name='follow'),
    path('<int:user_pk>/', views.detail, name='detail'),
    path('<int:user_pk>/delete/', views.delete, name='delete'),
    path('<int:user_pk>/update/', views.update, name='update'),
]
