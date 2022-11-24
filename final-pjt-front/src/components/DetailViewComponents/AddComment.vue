<template>
  <div class="comment-list">
    <hr>
    <div v-if="isLogin === true">
      <h5> 리뷰에 대한 댓글 남기기 </h5>
      <form @submit.prevent="addComment">
        <label for="add-comment"></label>
        <input type="textarea" id="add-comment" v-model="commentContent">
        <input type="submit">
      </form>
    </div>
    <div v-if="isLogin === false" class="need-login">
      <hr>
      <router-link :to="{ name: 'LoginView'}">댓글을 남기려면 로그인이 필요합니다.</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AddComment',
  data() {
    return {
      commentContent: null,
      movie_id: this.$route.params.id,
      isLogin: this.$store.getters.isLogin
    }
  },
  methods: {
    addComment() {
      const commentContent = this.commentContent
      const movie_id = this.movie_id
      const payload = {
        commentContent,
        movie_id,
      }
      this.$store.dispatch('addComment', payload)
      this.commentContent= null
    }
  }
}
</script>

<style scoped>
.need-login {
  text-align: center;
}
.comment-list {
  margin-left: 10%;
  margin-right: 10%;
}
</style>