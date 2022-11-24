<template>
  <div class="like-movies">
    <LikeMovieItem
    v-for="(userLikeMovie, index) in userLikeMovies"
    :key="index"
    :userLikeMovie="userLikeMovie"
    />
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
.like-movies{
  display: flex;
  flex-wrap: wrap;
}

</style>