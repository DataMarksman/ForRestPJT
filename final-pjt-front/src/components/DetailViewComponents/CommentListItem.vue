<template>
  <div class="background">
    <p>{{comment.user_id}}</p>
    <p>{{comment.content}}</p>
  </div>
</template>

<script>
export default {
  name: 'CommentListItem',
  props: {
    comment: Object
  }
}
</script>

<style>
.background {
  background-color: whitesmoke;
}
</style>