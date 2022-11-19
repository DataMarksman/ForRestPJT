<template>
  <div>
    <form @submit.prevent="logIn">
      <label for="user-id">ID</label>
      <input type="text" id="user-id" v-model="username">
      <label for="user-password">PASSWORD</label>
      <input type="text" id="user-password" v-model="password">
      <div>
        <input type="submit" value="로그인">
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    logIn() {
      const username = this.username
      const password = this.password
      
      const payload = {
        username: username,
        password: password,
      }
      this.$store.dispatch('logIn', payload)
    },
  },
}
</script>

<style>

</style>