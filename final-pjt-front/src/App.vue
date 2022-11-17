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
  }
}


</script>

<style>

</style>
