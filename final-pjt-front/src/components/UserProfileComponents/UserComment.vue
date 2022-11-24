<template>
  <div class="like-movies">
    <UserCommentItem
    v-for="(userLikeMovie, index) in userLikeMovies"
    :key="index"
    :userLikeMovie="userLikeMovie"
    />
  </div>
</template>

<script>
import UserCommentItem from '@/components/UserProfileComponents/UserCommentItem.vue'
export default {
  name:'UserComment',
  components: {
    UserCommentItem
    }
}
</script>

<style>

</style>