<template>
  <div class="detail-page">
    <img class="background-img" src="@/assets/backgroundimage.png" alt="">
    <h1> {{movie?.title}} ({{movie?.release_date}})</h1>
    <div class="movie-container">
      
      <div class="d-flex">
        <div class="img-container">
          <img class="detail-img" :src="movie.poster_path" alt="">
        </div>
        <div class="movie-detail-content">
          <p>제목 : {{ movie?.title }}</p>
          <MovieLike
          :movieLikeUsers ="movie.movie_like_users"
          :movie_id ="this.$route.params.id"
          />
        </div>
        
      </div>
      <div>
        <CommentList/>
      </div>
      <hr>
      <div>
        <AddComment/>
      </div>
      
      
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieLike from '@/components/DetailViewComponents/MovieLike'
import AddComment from '@/components/DetailViewComponents/AddComment'
import CommentList from '@/components/DetailViewComponents/CommentList'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'DetailView',
  components: {
    MovieLike,
    AddComment,
    CommentList,
  },
  data() {
    return {
      movie: {},
      movie_comment: null,
    }
  },
  created() {
    this.getMovieDetail()
  },
  methods: {
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.$route.params.id}`
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

<style scoped>
hr {
  color: black;
}
div {
  font-family: Arial, Helvetica, sans-serif;
  color: whitesmoke;
  text-shadow: -1px 0px black, 0px 1px black, 1px 0px black, 0px -1px black;
}
.detail-page{
  padding: 30px;
  
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
  width: 400px;
  height: 600px;
}
.detail-img {
  width: 100%;
  height: 100%;
}
.movie-detail-content {
  margin-left: 25px;
  text-align: center;
  
}
</style>