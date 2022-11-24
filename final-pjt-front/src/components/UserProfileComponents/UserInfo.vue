<template>
  <div class="profile-info-container">
    <div>
      <img class="profile-img" src="@/assets/personal_profile.png" alt="">
    </div>
    <br>
    <div class="nickname container">
      <div>
        <h3>{{userProfileInfo.username}}</h3>
      </div>
      <div v-if="userProfileInfo.pk !== currentUser.pk" @click="onFollow" class="follow-img-container">
        <img v-show="isFollow === false" class="follow-img" src="@/assets/follow.png" alt="">
        <img v-show="isFollow === true" class="follow-img" src="@/assets/currentfollow.png" alt="">
      </div>
    </div>
    <br>
    <div class="LFF">
      <div 
      class="element-pointer"
      @click="toLikePage"
      >
        <p>찜 영화</p>
        <p>{{userProfileInfo.user_like_movies.length}}</p>
      </div>
      <div 
      @click="toFollowPage"
      class="element-pointer">
        <p>팔로우</p>
        <p>{{userProfileInfo.followers.length}}</p>
      </div>
      <div @click="toFollowingPage"
      class="element-pointer">
        <p>팔로잉</p>
        <p>{{userProfileInfo.followings.length}}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name:'UserInfo',
  
  computed:{
    userProfileInfo() {
      return this.$store.state.userProfileInfo
    },
    currentUser() {
      return this.$store.state.currentUser
    },
    isFollow() {
      const Follow = this.userProfileInfo.followers.some((follower) => {
        return (follower.id === this.currentUser.pk) ? true: false;
      })
      return Follow
    }
  },
  methods: {
    toCommentPage() {
      const Comment = 'Comment'
      this.$store.commit('SHOW_PROFILE_INFO', Comment)
    },
    onFollow() {
      this.$store.dispatch('onFollow', this.userProfileInfo.pk)
    },
    toFollowPage() {
      const Follow = 'Follow'
      this.$store.commit('SHOW_PROFILE_INFO', Follow)
    },
    toFollowingPage() {
      const Following = 'Following'
      this.$store.commit('SHOW_PROFILE_INFO', Following)
    },
    toLikePage() {
      const Like = 'Like'
      this.$store.commit('SHOW_PROFILE_INFO', Like)
    },
  },
}
</script>

<style>
.profile-info-container{
  margin-top: 40px;
  margin-right: 20px;
  box-shadow: 3px 3px 3px black;
}
.follow-img-container{
  padding: 10px;
  width: 100px;
  height: auto;
  border-radius: 15px;
  border: 1px solid black;
  cursor: pointer;
  margin: auto;
}
.follow-img {
  width: 80%;
  
}
.LFF {
  display: flex;
  width: 180px;
}
.comment-link-box{
  background-color: white;
}
.rank-rate-movie-link{
  background-color: white;
}
.profile-img {
  max-width: 70px;
  margin: auto;
}
.element-pointer{
  cursor: pointer;
  margin-right:10px;
}
</style>