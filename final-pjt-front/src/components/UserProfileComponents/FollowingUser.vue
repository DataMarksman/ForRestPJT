<template>
  <div class="following-user">
    <FollowingUserItem
    v-for="(userFollowing, index) in userFollowings"
    :key="index"
    :userFollowing="userFollowing"
    />
  </div>
</template>

<script>
import FollowingUserItem from '@/components/UserProfileComponents/FollowingUserItem.vue'
export default {
  name:'FollowingUser',
  components: {
    FollowingUserItem,
  },
  props: {
    userFollowings : Array
  }
}
</script>

<style>
.following-user{
  display: flex;
  flex-wrap: wrap;
}
</style>