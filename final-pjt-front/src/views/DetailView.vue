<template>
  <div class="detail-page">
    <img class="background-img" src="@/assets/backgroundimage.png" alt="">
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
          <MovieLike
          :movie ="movie"
          />
        </div>
        
      </div>
      <div>
        <CommentList/>
      </div>
      
      <div>
        <AddComment/>
      </div>
      
      
    </div>
  </div>
</template>

<script>
import MovieLike from '@/components/DetailViewComponents/MovieLike'
import AddComment from '@/components/DetailViewComponents/AddComment'
import CommentList from '@/components/DetailViewComponents/CommentList'


export default {
  name: 'DetailView',
  components: {
    MovieLike,
    AddComment,
    CommentList,
  },
  data() {
    return {
      movie_id: this.$route.params.id,
      
    }
  },
  methods: {
  },
  created() {
    this.$store.dispatch('getMovieDetail', this.movie_id)
  },
  computed: {
    movie() {
      return this.$store.state.movieDetail
    },
    release_date() {
      return this.movie.release_date.substr(0, 4)
    },
  }
  
}
</script>

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
