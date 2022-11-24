<template>
<<<<<<< HEAD
  <div class="nav-bar">
    <div class="container">
      <div class="logo" @click="toHome">
        <img class="logo-img" src="@/assets/logo.png" alt="">
      </div>
      <router-link v-if="!this.$store.state.token" :to="{ name: 'SignupView' }">Signup</router-link>
      <router-link v-if="!this.$store.state.token" :to="{ name: 'LoginView' }">Login</router-link>
      <div @click="logOut">
        <p v-if="this.$store.state.token">Logout</p>
      </div>
      <div class="d-flex">
        <SearchBar/>
        <MiniProfile
        class="profile-icon"
        />
      </div>
=======
  <div class="nav-bar-container bg-dark p-1" style="--bs-bg-opacity: .9">
    <div class="nav-bar-left-container col-6">
      <div class="logo" @click="toHome">
        <img class="logo-img" src="@/assets/logo.png" alt="">
      </div>
      <div class="link-set">
        <router-link v-if="!this.$store.state.token" class="signup-link" :to="{ name: 'SignupView' }">Signup</router-link>
        <router-link v-if="!this.$store.state.token" class="login-link" :to="{ name: 'LoginView' }">Login</router-link>
        <div class="logout-link" @click="logOut">
          <p v-if="this.$store.state.token">Logout</p>
        </div>
      </div>
    </div>
    <div class="nav-bar-right-container d-flex justify-content-between col-6"> 
      
      <SearchBar/>
      <MiniProfile
      class="profile-icon"
      />
      
>>>>>>> 7db050a02491d7e8409747b92a8d304e626f1f3b
    </div>
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar'
import MiniProfile from '@/components/MiniProfile'
export default {
  name: 'NavBar',
  components: {
    SearchBar,
    MiniProfile
  },
  methods: {
    toHome() {
      this.$router.push({name: 'HomeView'})
    },
    logOut() {
      this.$store.dispatch('logOut')
    }
   
  }

}
</script>

<<<<<<< HEAD
<style>
.container {
=======
<style scoped>
.nav-bar-right-container{
  
  
}
div {
  font-family: Arial, Helvetica, sans-serif;
  color: whitesmoke;
  text-shadow: -1px 0px black, 0px 1px black, 1px 0px black, 0px -1px black;
}
.nav-bar-left-container {
  margin-left: 10px;
>>>>>>> 7db050a02491d7e8409747b92a8d304e626f1f3b
  display: flex;
  justify-content: space-between;
}
.logo {
  margin-top: 20px;
  width: 170px;
  height: auto;
  cursor: pointer;
}
.logo-img {
  width: 90%;
}
.nav-bar{
  padding-bottom: 10px;
  border-bottom: 1px solid black;
<<<<<<< HEAD
  
}
.profile-icon {
  cursor: pointer;
}
=======
  display: flex;
  justify-content: space-between;
  box-shadow: 7px 7px black;
}
.link-set {
  padding: 20px;
  padding-top: 30px;
  margin-right: 100px;
  
}
.signup-link {
  margin: 10px;
  margin-left: 20px;
  text-decoration-color: whitesmoke;
  text-decoration: none;
  font-size: 20px;
}
.login-link {
  margin: 10px;
  margin-left: 20px;
  text-decoration: none;
  font-size: 20px;
}
.logout-link {
  
  font-size: 20px;
  color: whitesmoke;
}
>>>>>>> 7db050a02491d7e8409747b92a8d304e626f1f3b
</style>