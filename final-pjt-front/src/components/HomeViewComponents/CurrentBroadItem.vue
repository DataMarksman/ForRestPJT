<template>
  <div>
    <img :src="currentBroadMovie.poster_path" alt="">
    <p>{{currentBroadMovie.title}}</p>
  </div>
</template>

<script>
export default {
  name:'CurrentBroadItem.vue',
  props: {
    currentBroadMovie: Object
  }
}
</script>

<style>

</style>