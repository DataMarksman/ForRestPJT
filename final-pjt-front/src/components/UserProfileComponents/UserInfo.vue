<template>
  <div class="">
    <div>
      <img class="profile-img" src="@/assets/user.png" alt="">
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
    <br>
  
    
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
      let following_users = this.userProfileInfo.followers
      const currentUser = this.currentUser.pk
      let Follow = following_users.some((user) => {
        console.log(user)
        console.log(currentUser)
        user.id == currentUser  
      })
      console.log(following_users)
      console.log(currentUser)
      console.log(Follow)
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
.follow-img-container{
  padding: 10px;
  width: 100px;
  height: auto;
  border-radius: 15px;
  border: 1px solid black;
  cursor: pointer;
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
}
.element-pointer{
  cursor: pointer;
  margin-right:10px;
}
</style>