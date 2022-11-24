<template>
  <div class="following-user-item-container">
    <div class="profile-img-box">
      <div class="profile-img-container">
        <img class="profile-img" src="@/assets/personal_profile.png" alt="">
      </div>
      <p class="profile-id-div">{{userFollow.username}}</p>
    </div>
    <div class="profile-img-box">
      <div class="profile-id-div-p">
      <p>팔로잉</p>
      <p>{{userFollow.followings.length}}</p>
      </div>
      <div class="profile-id-div">
        <p>팔로우</p>
        <p>{{userFollow.followers.length}}</p>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name:'FollowUserItem',
  props: {
    userFollow:Object
  }
}
</script>

<style>

</style>