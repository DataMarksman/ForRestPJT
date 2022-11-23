<template>
  <div class="image-box" @click="toDetail">
    <img class="image-thumbnail" :src="topRatedMovie.poster_path"  alt="">
    <p>{{topRatedMovie.title}}</p>
  </div>
</template>

<script>
export default {
  name:'PopularMoviesItem',
  props: {
    topRatedMovie: Object
  },
  methods: {
    toDetail() {
      const topRatedMovie = this.topRatedMovie
      this.$router.push({name: 'DetailView', params: { id: topRatedMovie.tmdb_id}})
    }
  }
}
</script>

<style>
.image-box {
  cursor: pointer;
  width:200px;
  height:300px;
  overflow:hidden;
  margin:0 auto;
}

.image-thumbnail {
    width:100%;
    height:100%;
    object-fit:cover;
}
</style>