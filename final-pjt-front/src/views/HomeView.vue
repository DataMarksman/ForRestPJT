<template>
  <div class="home-view">
    <img class="background-img" src="@/assets/backgroundimage.png" alt="">
    <CurrentBroad/>
    <br>
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
div {
  font-family: Arial, Helvetica, sans-serif;
  color: whitesmoke;
  text-shadow: -1px 0px black, 0px 1px black, 1px 0px black, 0px -1px black;
}
.home-view {
  margin-left: 10px;
  margin-top: 10px;
}
.board-line {
  margin-top: 20px;
  margin-left: 5px;
}
</style>