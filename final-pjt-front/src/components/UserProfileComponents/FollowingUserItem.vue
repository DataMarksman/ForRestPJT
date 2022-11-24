<template>
  <div class="following-user-item-container">
    <div class="profile-img-box">
      <div class="profile-img-container">
        <img class="profile-img" src="@/assets/personal_profile.png" alt="">
      </div>
      <p class="profile-id-div">{{userFollowing.username}}</p>
    </div>
    <div class="profile-img-box">
      <div class="profile-id-div-p">
      <p>팔로잉</p>
      <p>{{userFollowing.followings.length}}</p>
      </div>
      <div class="profile-id-div">
        <p>팔로우</p>
        <p>{{userFollowing.followers.length}}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name:'FollowingItem',
  props: {
    userFollowing: Object
  },
}
</script>

<style>
.following-user-item-container{
  width: 180px;
  box-shadow: 3px 3px 3px 3px black;
  margin-right: 10px;
  margin-bottom: 10px;
}
.profile-id-div-p{
  margin-right: 10px;
}
.profile-id-div{
  margin-left: 10px;
}
.profile-img-box {
  margin-top: 2px;
  display: flex;
  text-align: center;
  justify-content: center;
}
.profile-img-container {
  width: 30px;
  height: auto;
}
.profile-img{
  width: 100%;
  margin-right: 10px;
}
</style>