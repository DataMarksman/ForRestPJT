<template>
  <div>
    <div>
      <img class="profile-img" src="@/assets/user.png" alt="">
    </div>
    <br>
    <div>
      <h3>UserName</h3>
    </div>
    <br>
    <div class="LFF">
      <div 
      class="element-pointer"
      @click="toLikePage"
      >
        <p>좋아요</p>
        <p>(좋아요개수)</p>
      </div>
      <div 
      @click="toFollowPage"
      class="element-pointer">
        <p>팔로우</p>
        <p>(팔로우개수)</p>
      </div>
      <div @click="toFollowingPage"
      class="element-pointer">
        <p>팔로잉</p>
        <p>(팔로잉개수)</p>
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
    <div >
      <button class="rank-rate-movie-link element-pointer"
      @click="toUserScoreRatePage">평가한 영화 목록</button>
    </div>
  </div>
</template>

<script>
export default {
  name:'UserInfo',
  methods: {
    toLikePage() {
      this.$store.commit('TO_LIKE_PAGE')
    },
    toFollowPage() {
      this.$store.commit('TO_FOLLOW_PAGE')
    },
    toFollowingPage() {
      this.$store.commit('TO_FOLLOWING_PAGE')
    },
    toCommentPage() {
      this.$store.commit('TO_COMMENT_PAGE')
    },
    toUserScoreRatePage() {
      this.$store.commit('TO_SCORERATE_PAGE')
    },
  },
}
</script>

<style>
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