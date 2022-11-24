<template>
  <div class="following-user">
    <FollowUserItem
    v-for="(userFollow, index) in userFollows"
    :key="index"
    :userFollow="userFollow"
    />
  </div>
</template>

<script>
import FollowUserItem from '@/components/UserProfileComponents/FollowUserItem.vue'
export default {
  name: 'FollowUser',
  components: {
    FollowUserItem,
  },
  props: {
    userFollows: Array
  }
}
</script>

<style>

</style>