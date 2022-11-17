<template>
  <div>
    <h3>Forrest의 금주 추천 영화</h3>
    <br>
    <hr>
    <br>
    <RecommndMovieItem/>
  </div>
</template>

<script>
import RecommndMovieItem from '@/components/HomeViewComponents/RecommendMovieItem.vue'
export default {
  name: 'RecommendMovie',
  components: {
    RecommndMovieItem,
  },
}
</script>

<style>

</style>