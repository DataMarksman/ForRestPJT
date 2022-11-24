<template>
  <div id="app">
    <NavBar
    v-if="$route.name !== 'LoginView' && $route.name !== 'SignupView'"
    />
 
    <router-view
    />
  </div>
</template>
<script>
import NavBar from '@/components/NavBar.vue'

export default {
  name: 'App',
  components: {
    NavBar,
  },
  
}


</script>

<style>

.background-img {
  z-index: -1;
  position: absolute;
  top: 0px;
  left: 0px;
  width: 100%;
  height: 100vh;
  filter: blur(5px);
}
.background-img2 {
  z-index: -1;
  position: absolute;
  top: 100%;
  left: 0px;
  width: 100%;
  height: 100%;
  filter: blur(5px);
}
</style>
