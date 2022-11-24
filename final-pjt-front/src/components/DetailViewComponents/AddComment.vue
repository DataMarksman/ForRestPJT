<template>
  <div class="comment-list">
    <hr>
    <div v-if="isLogin === true">
      <h5> 리뷰에 대한 댓글 남기기 </h5>
      <form @submit.prevent="addComment">
        <label for="add-comment"></label>
        <input class="comment-input-bar" type="textarea" id="add-comment" v-model="commentContent">
        <input class="custom-btn btn-1" type="submit">
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
  padding-bottom: 7%;
}
.comment-input-bar{
  background-color: rgba(38, 48, 74);
  margin-right: 5px;
  color: whitesmoke;
}
.comment-input-bar-button{
  background-color: rgba(255, 150, 0);
}
.custom-btn {
  width: 80px;
  height: 30px;
  color: #fff;
  border-radius: 5px;
  padding: 5px 10px;
  font-family: 'Lato', sans-serif;
  font-weight: 500;
  background: transparent;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  display: inline-block;
   box-shadow:inset 2px 2px 2px 0px rgba(255,255,255,.5),
   7px 7px 20px 0px rgba(0,0,0,.1),
   4px 4px 5px 0px rgba(0,0,0,.1);
  outline: none;
}
.btn-1 {
  background: rgb(6,14,131);
  background: linear-gradient(0deg, rgba(6,14,131,1) 0%, rgba(12,25,180,1) 100%);
  border: none;
}
.btn-1:hover {
   background: rgb(0,3,255);
background: linear-gradient(0deg, rgba(0,3,255,1) 0%, rgba(2,126,251,1) 100%);
}
</style>