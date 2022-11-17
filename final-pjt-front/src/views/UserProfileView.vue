<template>
  <div class="user-profile">
    <div>
      <UserInfo/>
      <p>hi</p>
    </div>
    <div>
      <UserComment/>
      <FollowUser/>
      <FollowingUser/>
      <LikeMovie/>
      <UserScoreRate/>
    </div>
    
  </div>
  
</template>

<script>
import UserInfo from '@/components/UserProfileComponents/UserInfo'
import UserComment from '@/components/UserProfileComponents/UserComment.vue'
import FollowUser from '@/components/UserProfileComponents/FollowUser.vue'
import FollowingUser from '@/components/UserProfileComponents/FollowingUser.vue'
import LikeMovie from '@/components/UserProfileComponents/LikeMovie.vue'
import UserScoreRate from '@/components/UserProfileComponents/UserScoreRate.vue'
export default {
  name: 'UserProfileView',
  components: {
    UserInfo,
    UserComment,
    FollowUser,
    FollowingUser,
    LikeMovie,
    UserScoreRate
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
</style>