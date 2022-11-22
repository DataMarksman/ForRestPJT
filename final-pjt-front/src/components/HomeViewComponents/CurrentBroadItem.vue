<template>
  <div class="image-box" @click="toDetail">
    <img class="image-thumbnail" :src="currentBroadMovie.poster_path"  alt="">
    <p>{{currentBroadMovie.title}}</p>
  </div>
</template>

<script>
export default {
  name:'CurrentBroadItem.vue',
  props: {
    currentBroadMovie: Object
  },
  methods: {
    toDetail() {
      const currentBroadMovie = this.currentBroadMovie
      this.$router.push({name: 'DetailView', params: { id: currentBroadMovie.tmdb_id}})
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