<template>
  <div class="board-line">
    <section>
      <div class="content-list">
        <h1>현재 인기 있는 영화</h1>
        <br>
        <swiper
        class="swiper"
        :options="swiperOption">
          <swiper-slide 
            v-for="popularMovie in popularMovies"
            :key="popularMovie.id">
            <PopularMoviesItem :popularMovie="popularMovie"/>
          </swiper-slide>
          <div class="swiper-button-prev" slot="button-prev"></div>
          <div class="swiper-button-next" slot="button-next"></div>
        </swiper>
      </div>
    </section>
    <hr>
  </div>
</template>

<script>
import PopularMoviesItem from '@/components/HomeViewComponents/PopularMoviesItem'
import { Swiper, SwiperSlide } from "vue-awesome-swiper";
import "swiper/css/swiper.css";

export default {
  name: 'PopularMovies',
  components: {
    PopularMoviesItem,
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
    this.$store.dispatch('getPopularMovies')
  },
  computed: {
    popularMovies() {
    return this.$store.state.popularMovies
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

</style>