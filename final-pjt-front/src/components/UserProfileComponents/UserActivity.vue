<template>
  <div>
    <div>
      <div>
        <p>내 활동</p>
      </div>
      <div 
      class="flex-bar">
        <div class="element"
        @click="onShowComment">
          <p>내 댓글</p>
        </div>
        <div class="element"
        @click="onShowFollow">
          <p>팔로우</p>
        </div>
        <div class="element"
        @click="onShowFollwing">
          <p>팔로잉</p>
        </div>
        <div class="element"
        @click="onShowLikeMovie">
          <p>좋아요</p>
        </div>
        <div class="element"
        @click="onShowScoreRate">
          <p>평점</p>
        </div>
      </div>
    </div>
    <div>
      <UserComment
      v-show="userInfo.showComment === true"/>
      <FollowUser
      v-show="userInfo.showFollow === true"/>
      <FollowingUser
      v-show="userInfo.showFollowing === true"/>
      <LikeMovie
      v-show="userInfo.showLikeMovie === true"/>
      <UserScoreRate
      v-show="userInfo.showScoreRate === true"/>
    </div>
  </div>
</template>

<script>
import UserComment from '@/components/UserProfileComponents/UserComment.vue'
import FollowUser from '@/components/UserProfileComponents/FollowUser.vue'
import FollowingUser from '@/components/UserProfileComponents/FollowingUser.vue'
import LikeMovie from '@/components/UserProfileComponents/LikeMovie.vue'
import UserScoreRate from '@/components/UserProfileComponents/UserScoreRate.vue'

export default {
  name: 'UserActivity',
  components: {
    UserComment,
    FollowUser,
    FollowingUser,
    LikeMovie,
    UserScoreRate,
  },
  data() {
    return {
      userInfo: {
      showComment: true,
      showFollow: false,
      showFollowing: false,
      showLikeMovie: false,
      showScoreRate: false,
      },
    }
  },
  methods: {
    onShowComment() {
      this.userInfo.showComment = true
      this.userInfo.showFollow = false
      this.userInfo.showFollowing = false
      this.userInfo.showLikeMovie = false
      this.userInfo.showScoreRate = false
    },
    onShowFollow() {
      this.userInfo.showComment = false
      this.userInfo.showFollow = true
      this.userInfo.showFollowing = false
      this.userInfo.showLikeMovie = false
      this.userInfo.showScoreRate = false
    },
    onShowFollwing() {
      this.userInfo.showComment = false
      this.userInfo.showFollow = false
      this.userInfo.showFollowing = true
      this.userInfo.showLikeMovie = false
      this.userInfo.showScoreRate = false
    },
    onShowLikeMovie() {
      this.userInfo.showComment = false
      this.userInfo.showFollow = false
      this.userInfo.showFollowing = false
      this.userInfo.showLikeMovie = true
      this.userInfo.showScoreRate = false
    },
    onShowScoreRate() {
      this.userInfo.showComment = false
      this.userInfo.showFollow = false
      this.userInfo.showFollowing = false
      this.userInfo.showLikeMovie = false
      this.userInfo.showScoreRate = true
    },
    computed: {
      userInfo() {
        this.userInfo = this.$store.state.userInfo
        return this.userInfo
      }
    },
  }
}
</script>

<style>
.flex-bar{
  display: flex;
}
.element{
  margin-right: 10px;
  cursor: pointer;
}
</style>