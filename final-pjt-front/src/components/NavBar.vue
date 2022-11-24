<template>
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
    <div class="nav-bar-right-container col-6"> 
      <div class="d-flex justify-content-between">
        <SearchBar/>
        <MiniProfile
        class="profile-icon"
        />
      </div>
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

<style scoped>
.nav-bar-right-container{
  margin-right: 10px;
  box-shadow: 4px 4px 4px black;
}
div {
  font-family: Arial, Helvetica, sans-serif;
  color: whitesmoke;
  text-shadow: -1px 0px black, 0px 1px black, 1px 0px black, 0px -1px black;
}
.nav-bar-left-container {
  margin-left: 10px;
  display: flex;
  justify-content: space-between;
}
.logo {
  width: 150px;
  cursor: pointer;
}
.logo-img {
  max-width: 200px;
}
.nav-bar-container{
  padding-bottom: 10px;
  border-bottom: 1px solid black;
  display: flex;
  justify-content: space-between
}
.profile-icon {
  cursor: pointer;
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
  margin-right: 10px;
  font-size: 20px;
  color: whitesmoke;
}
</style>