<template>
  <div>
    <div>
      <img class="profile-img" src="@/assets/user.png" alt="">
    </div>
    <br>
    <div class="nickname container">
      <div>
        <h3>{{userInformation.nick_name}}</h3>
      </div>
      <div v-if="userInformation.pk !== currentUser.pk" @click="onFollow" class="follow-img-container">
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
        <p>{{userInformation.user_like_movies.length}}</p>
      </div>
      <div 
      @click="toFollowPage"
      class="element-pointer">
        <p>팔로우</p>
        <p>{{userInformation.followers.length}}</p>
      </div>
      <div @click="toFollowingPage"
      class="element-pointer">
        <p>팔로잉</p>
        <p>{{userInformation.followings.length}}</p>
      </div>
    </div>
    <br>
    <div>
      <button 
      class="comment-link-box element-pointer"
      @click="toCommentPage"
      >댓글 단 글</button>
    </div>
    <br>
    
  </div>
</template>

<script>
export default {
  name:'UserInfo',
  props: {
    userInformation: Object
  },
  computed:{
    currentUser() {
      return this.$store.state.currentUser
    },
    isFollow() {
      const following_users = this.userInformation.followers
      const currentUser = this.$store.state.currentUser?.pk
      return following_users.includes(currentUser)
    }
  },
  methods: {
    toCommentPage() {
      const Comment = 'Comment'
      this.$store.commit('SHOW_PROFILE_INFO', Comment)
    },
    onFollow() {
      this.$store.dispatch('onFollow', this.userInformation.pk)
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
}
.follow-img {
  width: 80%;
  
}
.LFF {
  display: flex;
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
}
</style>