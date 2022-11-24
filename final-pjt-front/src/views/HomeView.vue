<template>
  <div>
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