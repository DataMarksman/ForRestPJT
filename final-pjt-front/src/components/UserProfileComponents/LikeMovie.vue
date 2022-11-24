<template>
  <div>
    <LikeMovieItem
    v-for="(userLikeMovie, index) in userLikeMovies"
    :key="index"
    :userLikeMovie="userLikeMovie"/>
  </div>
</template>

<script>
import LikeMovieItem from '@/components/UserProfileComponents/LikeMovieItem.vue'
export default {
  name:'LikeMovie',
  components: {
    LikeMovieItem,
  },
  props: {
    userLikeMovies: Array
  },
}
</script>

<style>

</style>