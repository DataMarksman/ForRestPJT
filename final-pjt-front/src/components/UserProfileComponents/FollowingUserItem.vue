<template>
  <div>
    <p>FollwingUser</p>
  </div>
</template>

<script>
export default {
  name:'FollowingItem',
  props: {
    userFollow: Object
  },
  methods: {
    getFollowUsersInFo() {
      this.$store.dispatch('getFollowingUserInfo', this.userFollow)
    }
  }
}
</script>

<style>

</style>