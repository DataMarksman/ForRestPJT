<template>
  <div>
    <h1></h1>
    <div class="container">
      
      <div class="d-flex">
        <img :src="movie.poster_path" alt="">
        <div>
          <p>제목 : {{ movie?.title }}</p>
          <MovieLike
          :movieLikeUsers ="movie.movie_like_users"
          :movie_id ="this.$route.params.id"
          />
        </div>
        
      </div>
      
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

<style>

</style>