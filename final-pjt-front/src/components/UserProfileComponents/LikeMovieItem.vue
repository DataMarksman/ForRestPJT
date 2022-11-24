<template>
  <div @click="toMovie" class="like-movie-container">
    <div class="img-container">
      <img class="img-poster" :src="userLikeMovie.poster_path" alt="">
    </div>
  </div>

</template>

<script>
export default {
  name: 'LikeMovieItem',
  props: {
    userLikeMovie: Object
  },
  methods: {
    toMovie() {
      const movie_id = this.userLikeMovie.tmdb_id
      this.$router.push({name: 'DetailView', params: {id: movie_id }})
    }
  }
  
}
</script>

<style scoped>
.like-movie-form{
  display: flex;
  
}
.like-movie-container{
  display: flex;
  margin: 10px;
  cursor: pointer;
}
.img-container {
  width: 150px;
  height: auto;
}
.img-poster{
  width: 100%;
}
</style>