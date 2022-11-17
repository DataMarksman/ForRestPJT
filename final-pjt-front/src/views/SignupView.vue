<template>
  <div>
    <div>
      <form @submit.prevent="signUp">
        <label for="user-id">희망하는 ID를 입력해 주세요.</label>
        <input type="text" id="user-id" v-model="username">
        <label for="user-password1">희망하는 비밀번호를 입력해주세요.</label>
        <input type="text" id="user-password1">
        <label for="user-password2">희망하는 비밀번호를 다시 입력해 주세요.</label>
        <input type="text" id="user-password2">
        <div>
          <input type="submit" value="가입하기">
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name:'SignupView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signUp() {
      const payload = {
        username: this.username,
        password1: this.password1,
        password2: this.password2,
      }
      this.$store.dispatch('signUp', payload)
    }
  },
}
</script>

<style>

</style>