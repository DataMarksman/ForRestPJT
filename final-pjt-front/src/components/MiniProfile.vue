<template>
  <div>
    <div class="profile-icon-container" @click="toProfile">
      <img class="profile-icon" src="@/assets/personal_profile.png" alt="">
    </div>
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
.profile-icon-container {
  width: 60px;
  height: auto;
  cursor: pointer;
  margin-left: 50px;
  margin-top: 20px;
}
.profile-icon{
  width: 100%;
}

</style>