<template>
  <div>
    <h5> 리뷰에 대한 댓글 남기기 </h5>
    <form @submit.prevent="addComment">
      <label for="add-comment"></label>
      <input type="textarea" id="add-comment" v-model="commentContent">
      <input type="submit" 댓글 달기>
    </form>
  </div>
</template>

<script>
export default {
  name: 'AddComment',
  data() {
    return {
      commentContent: null,
      movie_id: this.$route.params.id
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

<style>

</style>