from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.movie_list),
    # path('<int:movie_id>/detail/', views.movie_detail),
    # path('<int:movie_id>/reviews/', views.create_review),
    # path('reviews/<int:review_id>/', views.review),
]