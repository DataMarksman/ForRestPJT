<template>
  <div @click="toProfile">
    <img class="profile-icon" src="@/assets/user.png" alt="">
  </div>
</template>

<script>
export default {
  name: 'MiniProfile',
  methods: {
    toProfile() {
      const id = this.$store.state.currentUser.pk
      this.$router.push({name: 'UserProfileView', params: {id:id }})
    },
  }
}
</script>

<style>
.profile-icon{
  width: 60px;
  height: 60px;
  margin-left: 20px;
  margin-right: 20px;
  
}

</style>