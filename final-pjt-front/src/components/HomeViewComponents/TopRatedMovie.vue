<template>
  <div class="board-line">
    <section>
      <div class="content-list">
        <h1>평점이 높은 영화 </h1>
        <br>
        <swiper
        class="swiper"
        :options="swiperOption">
          <swiper-slide 
            v-for="topRatedMovie in topRatedMovies"
            :key="topRatedMovie.id">
            <TopRatedMovieItem :topRatedMovie="topRatedMovie"/>
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
import TopRatedMovieItem from '@/components/HomeViewComponents/TopRatedMovieItem'
import { Swiper, SwiperSlide } from "vue-awesome-swiper";
import "swiper/css/swiper.css";

export default {
  name: 'PopularMovies',
  components: {
    TopRatedMovieItem,
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
    this.$store.dispatch('getTopRatedMovies')
  },
  computed: {
    topRatedMovies() {
    return this.$store.state.topRatedMovies
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