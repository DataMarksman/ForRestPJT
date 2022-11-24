<template>
  <div class="like-movies">
    <UserCommentItem
    v-for="(userComment, index) in userComments"
    :key="index"
    :userComment="userComment"
    />
  </div>
</template>

<script>
import UserCommentItem from '@/components/UserProfileComponents/UserCommentItem.vue'
export default {
  name:'UserComment',
  components: {
    UserCommentItem
    },
  props: {
    userComments: Array
  },
}
</script>

<style>

</style>