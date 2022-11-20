<template>
  <div>
    <div>
      <h4>현재 상영중인 영화</h4>
    </div>
    
    <br>
    <hr>
    <br>
    <div class="curent-broad-list">
      <CurrentBroadItem
      v-for="currentBroadMovie in currentBroadMovies"
      :key="currentBroadMovie.id"
      :currentBroadMovie="currentBroadMovie"
      />
    </div>
    <hr>
  </div>
</template>

<script>
import CurrentBroadItem from '@/components/HomeViewComponents/CurrentBroadItem.vue'

export default {
  name: 'CurrentBroad',
  components: {
    CurrentBroadItem,
  },
  created() {
    this.$store.dispatch('getMovieList')
  },
  computed: {
    currentBroadMovies() {
    return this.$store.state.currentBroadMovies
    }
  }
}
</script>

<style>
.curent-broad-list{
  display: flex;
}
</style>