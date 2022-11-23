<template>
  <div class="background">
    <div class="d-flex justify-content-between">
      <div class="comment-user-id">
        <p>{{comment.user_id}}</p>
      </div>
      <div v-if="currentUser?.pk === comment.user" class="d-flex">
        <div @click="commentAdjust" class="comment-adjust">
          <p>수정</p>
        </div>
        <div @click="commentDelete" class="comment-delete">
          <p>삭제</p>
        </div>
      </div>
    </div>
    <div class="comment-content">
      <p v-show="isAdjustShow === false">{{comment.content}}</p>
      <div class="d-flex">
        <form v-show="isAdjustShow === true" @submit.prevent="sendCommentAdjust">
          <label for="comment-content">댓글</label>
          <input class="text-area simple-margin" type="textarea" v-model="commentContent">
          <input class="simple-margin" type="submit" value='작성'>
          <button @click="turnoffAdjust" @submit.prevent v-show="isAdjustShow === true" class="simple-margin">취소</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CommentListItem',
  props: {
    comment: Object
  },
  data() {
    return {
      isAdjustShow: false,
      commentContent: this.comment.content,
      currentUser: this.$store.state.currentUser
    }
  },
  methods: {
    commentAdjust() {
      this.isAdjustShow = true
    },
    commentDelete() {
      const movie_id = this.comment.movie
      const comment_id = this.comment.id
      const payload = {
        movie_id,
        comment_id,
      }
      this.$store.dispatch('commentDelete', payload)
    },
    turnoffAdjust() {
      this.isAdjustShow = false
    },
    sendCommentAdjust() {
      const movie_id = this.comment.movie
      const comment_id = this.comment.id
      const user_id = this.$store.state.pk
      const content = this.commentContent
      const payload = {
        movie_id,
        comment_id,
        user_id,
        content,
      }
      this.$store.dispatch('sendCommentAdjust', payload)
      this.isAdjustShow = false
    },
  },

}

</script>

<style>
.comment-user-id{
  margin-left: 10px;
}
.background {
  background-color: whitesmoke;
  margin-bottom: 10px;
}
.comment-adjust{
  margin-left: 10px;
  cursor: pointer;
}
.comment-delete {
  margin-left: 10px;
  margin-right: 10px;
  cursor: pointer;
}
.comment-content{
  margin-left: 10px;
  margin-top: 5px;
}
.simple-margin {
  margin-left: 5px;
}
.simple-margin-right{
  margin-right: 15px;
}
.text-area {
  width: 300px;
  height: 30px;
}
</style>