<template>
  <div class="d-flex">
    <div class="d-flex img-conatiner">
      <div class="col-4"></div>
      <div @click="changeLike" class="like-container d-flex col-4">
        <div  class="img-div col-6">
          <div class="img-tag">
            <img class="img-content" v-show="isLikeShow === false" src="@/assets/like.png"  alt="">
            <img class="img-content" v-show="isLikeShow === true" src="@/assets/color_like.png" alt="">
          </div>
        </div>
        <div class="like-text col-6">
          <p> 좋아요!</p>
        </div>
      </div>
      <div class="col-4"></div>
    </div>
  </div>
</template>

<script>

export default {
  name:'MovieLike',
  data() {
    return {
      isLikeShow: false
    }
  },
  props: {
    movieLikeUsers: Array,
    movie_id: String,
  },
  methods: {
    changeLike() {
      if (this.isLikeShow === true) {
        this.isLikeShow = false
      } else {
        this.isLikeShow = true
      }
      this.sendLikeInfo()
    },
    sendLikeInfo() {
      const isLikeShow = this.isLikeShow
      const movie_id = this.$route.params.id
      const payload = {
        isLikeShow,
        movie_id
      }
      this.$store.dispatch('sendLikeInfo', payload)
    }
  },
  computed: {
    NumMovieLikeUsers() {
      return this.movieLikeUsers.length
    }
  }
}
</script>

<style scoped>

.img-div {
  font-size: 20px;
  border: black;
}
.img-conatiner {
  text-align: center;
  min-width: 700px;
}
.img-tag{
  width: 50px;
  height: 50px;
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