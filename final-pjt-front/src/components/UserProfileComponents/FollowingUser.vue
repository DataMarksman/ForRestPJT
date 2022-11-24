<template>
  <div>
    <FollowingUserItem
    v-for="(userFollow, index) in userFollows"
    :key="index"
    :userFollow="userFollow"
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
    userFollows:Array
  }
}
</script>

<style>

</style>