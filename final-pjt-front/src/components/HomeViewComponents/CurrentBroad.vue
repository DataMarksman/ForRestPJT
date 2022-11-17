<template>
  <div>
    <h4>현재 상영중인 영화</h4>
    <br>
    <hr>
    <br>
    <CurrentBroadItem/>
  </div>
</template>

<script>
import CurrentBroadItem from '@/components/HomeViewComponents/CurrentBroadItem.vue'
export default {
  name: 'CurrentBroad',
  components: {
    CurrentBroadItem,
    
  }
}
</script>

<style>

</style>