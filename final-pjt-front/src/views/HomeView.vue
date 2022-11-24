<template>
<<<<<<< HEAD
  <div>
=======
  <div class="home-view">
    <img class="background-img" src="@/assets/backgroundimage.png" alt="">
    <img class="background-img2" src="@/assets/backgroundimage.png" alt="">
>>>>>>> 7db050a02491d7e8409747b92a8d304e626f1f3b
    <CurrentBroad/>
    <RecommendMovie/>
  </div>
</template>

<script>
import RecommendMovie from '@/components/HomeViewComponents/RecommendMovie'
import CurrentBroad from '@/components/HomeViewComponents/CurrentBroad'

export default {
  name: 'HomeView',
  components: {
    CurrentBroad,
    RecommendMovie,
  },

}
</script>

<style>

</style>