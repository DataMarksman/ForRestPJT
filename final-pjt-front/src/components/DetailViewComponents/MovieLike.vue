<template>
  <div class="d-flex img-conatiner">
    <div class="col-4"></div>
    <div @click="sendLikeInfo" class="like-container d-flex col-4">
      <div  class="img-div col-6 ">
        <div class="img-tag">
          <img class="img-content" v-show="isLikeShow === false" src="@/assets/like.png"  alt="">
          <img class="img-content" v-show="isLikeShow === true" src="@/assets/color_like.png" alt="">
        </div>
      </div>
      <div class="like-text col-6">
        <p> 이 영화 좋아요!</p>
      </div>
    </div>
    <div class="col-4"></div>
  </div>
  
</template>

<script>

export default {
  name:'MovieLike',
  props: {
    movie : Object
  },
  methods: {
    sendLikeInfo() {
      if (this.$store.state.token === null){
        alert('좋아요 평가를 하시려면 로그인이 필요합니다.')
      } else {
        const movie_id = this.movie.id
        this.$store.dispatch('sendLikeInfo', movie_id)
      }
    }
  },
  computed: {
    isLikeShow() {
      const like_users = this.movie?.movie_like_users
      const currentUser = this.$store.state.currentUser?.pk
      return like_users.includes(currentUser)
    }
  }
}
</script>

<style scoped>
.like-container{
  border: 5px solid black;
  background-color: #000080;
  cursor: pointer;
}

.img-div {
  font-size: 20px;
  border: black;
}
.img-conatiner {
  text-align: center;
  width: auto;
}
.img-tag{
  width: 50px;
  height: auto;
  margin: auto;
  
}
.img-content {
  width: 100%;
  height: 100%;
}
.like-text {
  padding-top: 20px;
}
</style>