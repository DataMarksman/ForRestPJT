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

<style></style>