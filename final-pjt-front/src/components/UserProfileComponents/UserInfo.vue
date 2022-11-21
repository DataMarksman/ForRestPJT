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
      <div 
      class="element-pointer"
      @click="toLikePage"
      >
        <p>좋아요</p>
        <p>(좋아요개수)</p>
      </div>
      <div 
      @click="toFollowPage"
      class="element-pointer">
        <p>팔로우</p>
        <p>(팔로우개수)</p>
      </div>
      <div @click="toFollowingPage"
      class="element-pointer">
        <p>팔로잉</p>
        <p>(팔로잉개수)</p>
      </div>
    </div>
    <br>
    <div>
      <button 
      class="comment-link-box element-pointer"
      @click="toCommentPage"
    >댓글 단 글</button>
    </div>
    <br>
    <div >
      <button class="rank-rate-movie-link element-pointer"
      @click="toUserScoreRatePage">평가한 영화 목록</button>
    </div>
  </div>
</template>

<script>
export default {
  name:'UserInfo',
  methods: {
    toLikePage() {
      this.$store.commit('TO_LIKE_PAGE')
    },
    toFollowPage() {
      this.$store.commit('TO_FOLLOW_PAGE')
    },
    toFollowingPage() {
      this.$store.commit('TO_FOLLOWING_PAGE')
    },
    toCommentPage() {
      this.$store.commit('TO_COMMENT_PAGE')
    },
    toUserScoreRatePage() {
      this.$store.commit('TO_SCORERATE_PAGE')
    },
  },
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
.element-pointer{
  cursor: pointer;
}
</style>

<!-- 

프로필 사진을 웹 공유를 활용해 구현하기 위한 템플릿 코드

<template>
  <div>
    <h1>회원가입</h1>
    <form @submit.prevent="signUp" enctype="multipart/form-data">
      <label for="Image"> 프로필 사진 업로드: </label>
      <input type="file" name="Image" @change="fileChange" />
      <input type="submit" value="SignUp" />
    </form>
  </div>
</template>

<script>
import { getStorage, ref, uploadBytes, getDownloadURL } from "firebase/storage";

export default {
  name: "SignupView",
  data() {
    return {
      image: null,
    };
  },
  methods: {
    signUp() {
      const image = this.image;

      const payload = {
        image,
      };
      this.$store.dispatch("signUp", payload);
    },
    fileChange: function (e) {
      const nowImage = e.target.files[0];
      const date = new Date();
      const imgName = nowImage.name + date.toString();
      const storage = getStorage();
      const storageRef = ref(storage, imgName);
      uploadBytes(storageRef, nowImage).then(() => {
        getDownloadURL(ref(storage, imgName)).then((url) => {
          console.log(url);
          this.image = url;
        });
      });
    },
  },
};
</script>

<style></style> -->