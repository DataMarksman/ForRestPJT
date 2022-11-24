<template>
  <div>
    <div>
      <div>
        <p>내 활동</p>
      </div>
      <div 
      class="flex-bar">
        <div class="element"
        @click="toCommentPage">
          <p>내 댓글</p>
          <p v-show="showProfile === 'Comment'"> ({{userInformation.comment_set.length}})</p>
        </div>
        <div class="element"
        @click="toFollowPage">
          <p>팔로우</p>
          <p v-show="showProfile === 'Follow'"> ({{userInformation.followers.length}})</p>
        </div>
        <div class="element"
        @click="toFollowingPage">
          <p>팔로잉</p>
          <p v-show="showProfile === 'Following'"> ({{userInformation.followings.length}})</p>
        </div>
        <div class="element"
        @click="toLikePage">
          <p>좋아요</p>
          <p v-show="showProfile === 'Like'"> ({{userInformation.user_like_movies.length}})</p>
        </div>
      </div>
    </div>
    <div>
      <UserComment
      v-show="showProfile === 'Comment'"/>
      <FollowUser
      v-show="showProfile === 'Follow'"/>
      <FollowingUser
      v-show="showProfile === 'Following'"/>
      <LikeMovie
      v-show="showProfile === 'Like'"
      :userLikeMovies="userInformation.user_like_movies"
      />
    </div>
  </div>
</template>

<script>
import UserComment from '@/components/UserProfileComponents/UserComment.vue'
import FollowUser from '@/components/UserProfileComponents/FollowUser.vue'
import FollowingUser from '@/components/UserProfileComponents/FollowingUser.vue'
import LikeMovie from '@/components/UserProfileComponents/LikeMovie.vue'

export default {
  name: 'UserActivity',
  components: {
    UserComment,
    FollowUser,
    FollowingUser,
    LikeMovie,
  },
  props: {
    userInformation: Object
  },
  methods: {
    toCommentPage() {
      const Comment = 'Comment'
      this.$store.commit('SHOW_PROFILE_INFO', Comment)
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
  computed: {
    showProfile() {
      return this.$store.state.showProfileInfo
    }
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
  display: flex;
}
</style>