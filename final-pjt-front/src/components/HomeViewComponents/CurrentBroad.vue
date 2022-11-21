<template>
  <div>
    <section>
      <div class="content-list">
        <h1>현재 상영중인 영화</h1>
        <div class="slider">
          <CurrentBroadItem
          v-for="currentBroadMovie in currentBroadMovies"
          :key="currentBroadMovie.id"
          :currentBroadMovie="currentBroadMovie"
          />
        </div>
        <div class="prev" @click="preSlide"><i class="fa-solid fa-angle-right prev-arrow">next</i></div>
        <div class="next" @click="nextSlide"><i class="fa-solid fa-angle-right">pre</i></div>
      </div>
    </section>
    <hr>
  </div>
</template>

<script>
import CurrentBroadItem from '@/components/HomeViewComponents/CurrentBroadItem.vue'

export default {
  name: 'CurrentBroad',
  components: {
    CurrentBroadItem,
  },
  created() {
    this.$store.dispatch('getMovieList')
  },
  computed: {
    currentBroadMovies() {
    return this.$store.state.currentBroadMovies
    }
  },
  methods: {
    nextSlide() {
      const slider = document.querySelector('.slider')
      const offsetX = slider.offsetwidth;
      slider.scrollBy(offsetX, 0)
    },
    preSlide() {
      const slider = document.querySelector('.slider')
      const offsetX = slider.offsetwidth;
      slider.scrollBy(-offsetX,0)
    }
  }
  
}
</script>

<style>
section .content-list {
  margin-bottom: 3rem;
  position: relative;
}
section .content-list h1 {
  margin-left: 2rem;
  margin-bottom: 1rem;
  margin-top: 0.5rem;
}
section .content-list .slider {
  display: flex;
  gap: 0.5rem;
  overflow-x: scroll;
  scroll-behavior: smooth;
}
section .content-list .slider::-webkit-scrollbar {
  display: none;
}
section .content-list .slider .item {
  min-width: 250px;
  height: 150px;
  background: #262626;
  background: linear-gradient(312deg, #262626 0%, #333333 54%, #2a2a2a 100%);
  border-radius: 5px;
}
section .content-list .slider .item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
section .content-list .prev-arrow {
  transform: rotateY(180deg);
}
section .content-list .prev {
  font-size: 3rem;
  position: absolute;
  top: 50%;
  left: 10px;
  transform: translateY(-10px);
  cursor: pointer;
}
section .content-list .next {
  font-size: 3rem;
  position: absolute;
  top: 50%;
  right: 10px;
  transform: translateY(-10px);
  cursor: pointer;
}

</style>