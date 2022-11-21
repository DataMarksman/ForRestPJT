<template>
  <div class="user-profile">
    <div>
      <UserInfo/>
      <p>hi</p>
    </div>
    <div class="user-activity">
      <UserActivity/>
    </div>
    
  </div>
  
</template>

<script>
import UserInfo from '@/components/UserProfileComponents/UserInfo'
import UserActivity from '@/components/UserProfileComponents/UserActivity.vue'
export default {
  name: 'UserProfileView',
  components: {
    UserInfo,
    UserActivity,
  }
}
</script>

<style>
.user-profile{
  padding-top: 30px;
  padding-left: 30px;
  padding-right: 30px;
  background-color: whitesmoke;
  display: flex;
  text-align: center;
}
.user-activity{
  text-align: left;
  margin-left: 10px;
}
</style>
