<template>
  <div>
    <img src="@/assets/like.png" @click="changeLike" alt="">
    <p>{{NumMovieLikeUsers}}</p>
  </div>
</template>

<script>

export default {
  name:'MovieLike',
  props: {
    movieLikeUsers: Array,
    movie_id: String,
  },
  methods: {
    changeLike() {
      this.$store.dispatch('changeLike', this.movie_id)
    }
  },
  computed: {
    NumMovieLikeUsers() {
      return this.movieLikeUsers.length
    }
  }
}
</script>

<style>

</style>