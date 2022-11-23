from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    # 영화 관련 urls
    path('', views.movie_list, name='movie_index'),  # 영화 전체 리스트 -> get 과 post(만드는 과정에서 특이값 입력용)
    path('<int:movie_pk>/', views.movie_detail, name='movie_detail'), # 영화 상세 페이지 pk(tmdb_id)를 기반으로 해당 영화의 디테일 페이지 도출
    path('<int:movie_pk>/like/', views.movie_like, name='movie_like'), # 영화에 대한 유저의 좋아요를 반영한다.
    path('search/<str:word>/', views.movie_search, name='movie_search'), # 영화 검색하기
    path('newmovie/', views.get_new_movie, name='new_movie'), # 현재 상영중인 영화 목록을 반환한다.
    path('genremovie/<str:genre_name>/', views.get_genre_movie, name='genre_movie'), # 장르별 영화를 도출한당

    # 댓글 관련 urls
    path('<int:movie_pk>/comments/', views.comment_list),
    path('<int:movie_pk>/comments/create/', views.comment_create),
    path('<int:movie_pk>/comments/<int:comment_pk>/', views.comment_detail),
    path('<int:movie_pk>/comments/<int:comment_pk>/like/', views.comment_like),
    
    # # 필수 작성
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # # optional UI
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
