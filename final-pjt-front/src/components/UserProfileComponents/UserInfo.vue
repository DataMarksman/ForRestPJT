<template>
  <div>
    <div>
      <img class="profile-img" src="@/assets/user.png" alt="">
    </div>
    <br>
    <div>
      <h3>UserName</h3>
    </div>
    <br>
    <div class="LFF">
      <div>
        <p>좋아요</p>
        <p>(좋아요개수)</p>
      </div>
      <div>
        <p>팔로우</p>
        <p>(팔로우개수)</p>
      </div>
      <div>
        <p>팔로잉</p>
        <p>(팔로잉개수)</p>
      </div>
    </div>
    <br>
    <div>
      <button class="comment-link-box">댓글 단 글</button>
    </div>
    <br>
    <div>
      <button class="rank-rate-movie-link">평가한 영화 목록</button>
    </div>
  </div>
</template>

<script>
export default {
  name:'UserInfo',
}
</script>

<style>
.LFF {
  display: flex;
}
.comment-link-box{
  background-color: white;
}
.rank-rate-movie-link{
  background-color: white;
}
.profile-img {
  max-width: 70px;
}
</style>