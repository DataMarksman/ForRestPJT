from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.response import HttpResponse
from .models import *
from .serializer import *
from datetime import date, timedelta
import random
import requests


# # 로그인 여부에 따라 데코 붙이려면 이거 살리고
# # @permission_classes([IsAuthenticated])
# @api_view(['GET'])
# def movie_list(request):
#     if request.method == 'GET':
#         Movies = get_list_or_404(Movie)
#         serializer = MovieListSerializer(Movies, many=True)
#         return Response(serializer.data)

# @api_view(['GET'])
# def box_movie_list(request):
#     if request.method == 'GET':
#         BoxMovies = get_list_or_404(Movie)
#         serializer = BoxMovieListSerializer(BoxMovies, many=True)
#         return Response(serializer.data)




# # 로그인 여부에 따라 데코 붙이려면 이거 살리고
# # @permission_classes([IsAuthenticated])
# @api_view(['GET', 'POST'])
# def comment_list(request):
#     if request.method == 'GET':
#         Comments = get_list_or_404(Movie)
#         serializer = CommentListSerializer(Comments, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = CommentSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)


# genre_dict = {
#     28: '액션',
#     12: '어드밴쳐',
#     16: '애니매이션',
#     35: '코미디',
#     80: '범죄',
#     99: '다큐멘터리',
#     18: '드라마',
#     10751: '가족',
#     14: '판타지',
#     36: '역사',
#     27: '공포',
#     10402: '음악',
#     9648: '미스터리',
#     10749: '로맨스',
#     878: 'SF',
#     10770: 'TV 영화',
#     53: '스릴러',
#     10752: '전쟁',
#     37: '서부'
# }

# def get_box_office():
#     yesterday = date.today() - timedelta(1)
#     # 한국 컨텐츠 진흥원에서 지금 상영중인 영화를 불러오겠습니다.   
#     BASE = "https://www.kobis.or.kr/"
#     path = "kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml"
#     params = {
#         'key': "ce10aa520981b26cce4565d991bf011b&target",
#         'DT' : yesterday
#     }
#     response = requests.get(BASE+path,params=params).json()
#     go_to_db = response['results']

#     # db 저장하겠슴다
#     data = []
#     for i in go_to_db:
#         movie_data = {}
#         movie_data['box_rank'] = i['rank']
#         movie_data['title'] = i['movieNm']
#         data.append(movie_data)
#     return data



@api_view(['GET'])
def movie_list(request):
    Movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(Movies, many=True)
    return Response(serializer.data)
