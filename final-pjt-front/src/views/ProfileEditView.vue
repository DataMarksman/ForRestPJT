<template>
  <div>
    <h1>프로필 이미지 삽입</h1>
    <form @submit.prevent="uploadImge" enctype="multipart/form-data">
      <label for="Image"> 프로필 사진 업로드: </label>
      <input type="file" name="Image" @change="fileChange" />
      <input type="submit" value="이미지 업로드" />
    </form>
  </div>
</template>

<script>
import { getStorage, ref, uploadBytes, getDownloadURL } from "firebase/storage";

export default {
  name: "ProfileEditView",
  data() {
    return {
      image: null,
    };
  },
  methods: {
    uploadImge() {
      const image = this.image;
      this.$store.dispatch("uploadImge", image);
    },
    fileChange(e) {
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