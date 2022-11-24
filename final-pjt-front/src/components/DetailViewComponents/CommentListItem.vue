<template>
  <div class="background">
    <div class="d-flex justify-content-between">
      <div class="comment-user-id">
        <p class="cursor-pointer" @click="toProfile">{{comment.user}}</p>
        <hr class="border-line">
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
    
    <div  class="comment-content d-flex">
      <div v-show="isAdjustShow === false" class="">
        <p >{{comment.content}}</p>
        <hr class="border-line">
        <div @click="commentLike" class="d-flex like-box">
          <div class="img-container ">
            <img class="img-content" v-if="isCommentLike === false" src="@/assets/space_heart.png" alt="">
            <img class="img-content" v-if="isCommentLike === true" src="@/assets/active_heart.png" alt="">
          </div>
          <div>
            <p class="like-text">좋아요</p>
          </div>
          <div>
            <p class="like-text">{{comment.comment_like_users.length}}</p>
          </div>
        </div>
      </div>
    
      <div class="d-flex">
        <form v-show="isAdjustShow === true" @submit.prevent="sendCommentAdjust">
          <label for="comment-content">댓글 수정</label>
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
      currentUser: this.$store.state.currentUser,
      
    }
  },
  methods: {
    toProfile() {
      this.$router.push({name: 'UserProfileView', params: {id: this.comment.user }})
    },
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
    commentLike() {
      if (this.$store.state.token === null) {
        alert('좋아요를 누르려면 로그인이 필요합니다.')
      } else{const movie_id = this.comment.movie
      const comment_id = this.comment.id
      const payload = {
        movie_id,
        comment_id
      }
      this.$store.dispatch('commentLike', payload)
      }
    }
  },
  computed: {
    isCommentLike() {
      const like_comment = this.comment?.comment_like_users
      const currentUser = this.$store.state.currentUser?.pk
      return like_comment.includes(currentUser)
    }
  }
}

</script>

<style >
.cursor-pointer{
  cursor:pointer;
}
.like-box {
  cursor: pointer;
}
.border-line {
  color: black;
  margin-top: 0px;
  box-shadow: 0 1px 0 black;
}
.like-text{
  margin-left: 10px;
}
.img-container{
  width: 20px;
  margin-bottom: 10px;
}
.img-content {
  width:100%
}
.comment-user-id{
  margin-left: 10px;
}
.background {
  background-color: rgba(37, 48, 74);
  margin-bottom: 10px;
  border-radius: 15px;
  box-shadow: 5px 5px 5px black;
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
  color: rgba(37, 48, 74);
}

</style>