<template>
  <div>
    <img class="wave" src="https://raw.githubusercontent.com/sefyudem/Responsive-Login-Form/master/img/wave.png">
    <div class="login-container">
      <div class="img">
        <img src="https://raw.githubusercontent.com/sefyudem/Responsive-Login-Form/master/img/bg.svg">
      </div>
    <div class="login-content">

      <form class="login-form" @submit.prevent="signUp">
        <img src="https://raw.githubusercontent.com/sefyudem/Responsive-Login-Form/master/img/avatar.svg">
        <h2 class="login-title">signup page</h2>
            <div class="input-div one">
                <div class="i">
                  <i class="fas fa-user"></i>
                </div>
                <div class="div">
                  <h5>Username</h5>
                  <input 
                  type="text" class="input" 
                  v-model="username">
                </div>
            </div>
            <div class="input-div pass">
                <div class="i"> 
                  <i class="fas fa-lock"></i>
                </div>
                <div class="div">
                  <h5>Password</h5>
                  <input type="password" class="input"
                  v-model="password">
                </div>
            </div>
            <div class="input-div pass">
                <div class="i"> 
                  <i class="fas fa-lock"></i>
                </div>
                <div class="div">
                  <h5>Confirm Password</h5>
                  <input type="password" class="input"
                  v-model="password">
                </div>
            </div>
            <input type="submit" class="login-btn" value="signup">
            <hr>
          </form>
        </div>
        
      </div>
    <!-- <form @submit.prevent="signUp">
      <label for="user-id">희망하는 ID를 입력해 주세요.</label>
      <input type="text" id="user-id" v-model="username">
      
      <label for="user-password1">희망하는 비밀번호를 입력해주세요.</label>
      <input type="text" id="user-password1" v-model="password1">
      
      <label for="user-password2">희망하는 비밀번호를 다시 입력해 주세요.</label>
      <input type="text" id="user-password2"  v-model="password2">
      
      
      <input type="submit" value="가입하기">
    </form> -->
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
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username: username,
        password1: password1,
        password2: password2,
      }
      this.$store.dispatch('signUp', payload)
    }
  },
}
</script>

<style>

</style>