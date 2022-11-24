<template>
  <div class="image-box" @click="toDetail">
    <img class="image-thumbnail" :src="popularMovie.poster_path"  alt="">
    <p>{{popularMovie.title}}</p>
  </div>
</template>

<script>
export default {
  name:'PopularMoviesItem',
  props: {
    popularMovie: Object
  },
  methods: {
    toDetail() {
      const popularMovie = this.popularMovie
      this.$router.push({name: 'DetailView', params: { id: popularMovie.tmdb_id}})
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