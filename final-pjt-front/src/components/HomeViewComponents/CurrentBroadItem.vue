<template>
  <div class="detail-box" @click="toDetail">
    <img :src="currentBroadMovie.poster_path" alt="">
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
.detail-box{
  cursor: pointer;
}
</style>