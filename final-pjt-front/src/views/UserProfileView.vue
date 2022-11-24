<template>
  <div class="user-profile">
    <div>
      <UserInfo
      :userInformation="userInformation"/>
      <p>hi</p>
    </div>
    <div class="user-activity">
      <UserActivity
      :userInformation="userInformation"/>
    </div>
  </div>
  
</template>

<script>
import UserInfo from '@/components/UserProfileComponents/UserInfo'
import UserActivity from '@/components/UserProfileComponents/UserActivity.vue'
export default {
  name: 'UserProfileView',
  data() {
    return {
      profileUserId: this.$route.params.id
    }
  },
  created() {
    this.$store.dispatch('getUserProfile', this.profileUserId)
  },
  components: {
    UserInfo,
    UserActivity,
  },
  computed: {
    userInformation() {
      return this.$store.state.userProfileInfo
    }
  }
}
</script>

<style>
.user-profile{
  padding-top: 30px;
  padding-left: 15%;
  padding-right: 15%;
  background-color: whitesmoke;
  display: flex;
  text-align: center;
}
.user-activity{
  text-align: left;
  margin-left: 10px;
}
</style>
