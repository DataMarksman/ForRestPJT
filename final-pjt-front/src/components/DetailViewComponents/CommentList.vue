<template>
  <div>
    <CommentListItem
    v-for="comment in getCommentList"
    :key="comment.id"
    :comment="comment"
    />
  </div>
</template>

<script>
import CommentListItem from '@/components/DetailViewComponents/CommentListItem'
export default {
  name: 'CommentList',
  components: {
    CommentListItem,
  },
  computed: {
    getCommentList() {
      return this.$store.state.movieCommentList
    }
  },
  created() {
    const movie_id = this.$route.params.id
    this.$store.dispatch('getCommentList', movie_id)
  }
}
</script>

<style>

</style>