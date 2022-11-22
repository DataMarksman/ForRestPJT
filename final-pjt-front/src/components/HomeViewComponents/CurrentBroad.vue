<template>
  <div class="board-line">
    <section>
      <div class="content-list">
        <h1>현재 상영중인 영화</h1>
        <br>
        <swiper
        class="swiper"
        :options="swiperOption">
          <swiper-slide 
            v-for="currentBroadMovie in currentBroadMovies"
            :key="currentBroadMovie.id">
            <CurrentBroadItem :currentBroadMovie="currentBroadMovie"/>
          </swiper-slide>
          <!-- <div
          class="swiper-pagination"
          slot="pagination"
          >
          </div> -->
          <div class="swiper-button-prev" slot="button-prev"></div>
          <div class="swiper-button-next" slot="button-next"></div>
        </swiper>
      </div>
    </section>
    <hr>
  </div>
</template>

<script>
import CurrentBroadItem from '@/components/HomeViewComponents/CurrentBroadItem.vue'
import { Swiper, SwiperSlide } from "vue-awesome-swiper";
import "swiper/css/swiper.css";

export default {
  name: 'CurrentBroad',
  components: {
    CurrentBroadItem,
    Swiper,
    SwiperSlide,
  },
  data() {
    return {
      swiperOption: { 
        slidesPerView: 6, 
        spaceBetween: 10, 
        loop: true, 
        navigation: { 
            nextEl: '.swiper-button-next', 
            prevEl: '.swiper-button-prev' 
        } 
      },
    }
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
/* .content-list {
  display: flex;
} */

</style>