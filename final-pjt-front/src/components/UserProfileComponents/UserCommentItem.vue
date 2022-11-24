<template>
  <div class="user-comment-box">
    <div class="comment-img-box">
      <img class="comment-movie-img" :src="userComment.movie.poster_path" alt="">
    </div>
    <div class="comment-content-container">
      <div>
        <p>{{userComment.movie.title}}</p>
      </div>
      <div>
        <p>내가 쓴 리뷰: {{userComment.content}}</p>
      </div>
    </div>
    
    
  </div>
</template>

<script>
export default {
  name:'UserCommentItem',
  props: {
    userComment: Object
  }
}
</script>

<style>
.user-comment-box{
  display:flex;
  margin-left: 10px;
  margin-top: 10px;
  box-shadow: 3px 3px 3px black;
  background-color: rgba(16 19 34) ;
  border-radius: 5px;
  
}
.comment-img-box{
  width: 90px;
  height: auto;
  position: relative;
  
}
.comment-movie-img{
  width: 100%;
  
}
.comment-content-container{
  margin-top: 10px;
  margin-left: 10px;
  margin-right: 10px;
}
</style>