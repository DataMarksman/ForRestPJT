<template>
<<<<<<< HEAD
  <div>
    <h1></h1>
    <div class="container">
      
      <div class="d-flex">
        <img :src="movie.poster_path" alt="">
        <div>
          <p>제목 : {{ movie?.title }}</p>
=======
  <div class="detail-page">
    
    
    <h1> {{movie?.title}} ({{release_date}})</h1>
    <div class="movie-container">
      
      <div class="d-flex">
        <div class="img-container col-4">
          <img class="detail-img" :src="movie?.poster_path" alt="">
        </div>
        <div class="movie-detail-content col-8">
          <p class="detail-title"><b>{{ movie?.title }}</b></p>
          <div class="row triple-container">
            <div class="d-flex">
              <div class="col-4">
                <div>
                  <p>평점</p>
                </div>
                <div class="star-container">
                  <img class="img-star" src="@/assets/star.png" alt="">
                </div>
                <div>
                  <p><b>{{movie?.vote_average}}</b></p>
                </div>
              </div>
              <div class="col-4">
                <div>
                  <p>장르</p>
                </div>
                <div class="star-container">
                  <img class="img-star" src="@/assets/genres.png" alt="">
                </div>
                <div>
                  <b
                  class="genre-font"
                  v-for="(genre, index) in movie.genre"
                  :key="index"> {{genre, }} </b>
                </div>
              </div>
              <div class="col-4">
                <div>
                  <p>사용자 추천수</p>
                </div>
                <div class="star-container">
                  <img class="img-star" src="@/assets/color_like.png" alt="">
                </div>
                <div>
                  <p><b>{{movie?.movie_like_users.length}}</b></p>
                </div>
              </div>
            </div>
            
          </div>
          <div>
            {{movie?.overview}}
          </div>
>>>>>>> 7db050a02491d7e8409747b92a8d304e626f1f3b
          <MovieLike
          :movieLikeUsers ="movie.movie_like_users"
          :movie_id ="this.$route.params.id"
          />
        </div>
        
      </div>
<<<<<<< HEAD
=======
      <div>
        <CommentList/>
      </div>
      
      <div>
        <AddComment/>
      </div>
>>>>>>> 7db050a02491d7e8409747b92a8d304e626f1f3b
      
      <div>
      </div>
      
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieLike from '@/components/DetailViewComponents/MovieLike'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'DetailView',
  components: {
    MovieLike
  },
  data() {
    return {
      movie: {},
      
    }
  },
  created() {
    this.getMovieDetail()
  },
  methods: {
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/${this.$route.params.id}`
      })
        .then((res) => {
          this.movie = res.data
        })
        .catch((err) => {
        console.log(err)
        })
    },
    clickLike() {
      
    }
  },
  
}
</script>

<<<<<<< HEAD
<style>

</style>
=======
<style scoped>
.genre-font{
  font-size: 25px;
}
.detail-title{
  font-size: 30px;
}
.triple-container{
  font-size: 40px;
}
.star-container {
  width: 20%;
  margin: auto;
}
.img-star {
  width: 100%;
  height: auto;
}
hr {
  color: black;
}
div {
  font-family: Arial, Helvetica, sans-serif;
  color: rgb(226, 226, 226);
  text-shadow: -1px 0px black, 0px 1px black, 1px 0px black, 0px -1px black;
}
.detail-page{
  padding-left: 10%;
  padding-right: 10%;
  background-color: rgba(16 19 34) ;
}
.background-img {
  z-index: -1;
  position: absolute;
  top: 0px;
  left: 0px;
  width: 100%;
  height: 100%;
  filter: blur(5px);
}
.img-container {
  /* width: 400px;
  height: 600px; */
  width: 20%;
}
.detail-img {
  width: 90%;
  height: auto;
}
.movie-detail-content {
  margin-left: 4%;
  margin-right: 4%;
  text-align: center;
  
}
</style>
>>>>>>> 7db050a02491d7e8409747b92a8d304e626f1f3b
