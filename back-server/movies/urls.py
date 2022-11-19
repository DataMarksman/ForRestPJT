from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views




app_name = 'movies'
urlpatterns = [
    # 영화 관련 urls
    path('', views.movie_list),  # 영화 전체 리스트 -> get 과 post(만드는 과정에서 특이값 입력용)
    path('<int:movie_pk>/', views.movie_detail), # 영화 상세 페이지 pk(tmdb_id)를 기반으로 해당 영화의 디테일 페이지 도출
    




    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('<int:movie_pk>/comments/', views.comment_create),
    
    # # 필수 작성
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # # optional UI
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
