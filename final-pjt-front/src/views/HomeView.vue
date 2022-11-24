<template>
  <div class="home-view">
    <img class="background-img" src="@/assets/backgroundimage.png" alt="">
    <img class="background-img2" src="@/assets/backgroundimage.png" alt="">
    <CurrentBroad/>
    <br>
    <TopRatedMovie/>
    <br>
    <PopularMovies/>
  </div>
</template>

<script>
import PopularMovies from '@/components/HomeViewComponents/PopularMovies'
import CurrentBroad from '@/components/HomeViewComponents/CurrentBroad'
import TopRatedMovie from '@/components/HomeViewComponents/TopRatedMovie'
export default {
  name: 'HomeView',
  components: {
    CurrentBroad,
    PopularMovies,
    TopRatedMovie,
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