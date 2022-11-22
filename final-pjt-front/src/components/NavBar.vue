<template>
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

<style>
.container {
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
.nav-bar{
  padding-bottom: 10px;
  border-bottom: 1px solid black;
  
}
.profile-icon {
  cursor: pointer;
}
</style>