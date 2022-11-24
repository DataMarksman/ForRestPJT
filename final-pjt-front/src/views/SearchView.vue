<template>
  <div class="search-view">
    <img class="background-img" src="@/assets/backgroundimage.png" alt="">
    <div id="#">
      <div class="#">검색결과</div>
       <hr class="border-line">
       <h3></h3>
       <p><b>'{{getKeyWord}}'의 검색결과 입니다.</b></p>
    </div>
    <SearchResult
    :keyword ="getKeyWord"
    /> 
  </div>
</template>

<script>
import SearchResult from '@/components/SearchResult'
export default {
  name:'SearchView',
  components: {
    SearchResult,
  },
  computed: {
    getKeyWord() {
      return this.$route.params.keyword
    }
  }
  
 
}
</script>

<style scoped>
.search-view{
  margin-left: 15px;
}
.border-line {
  border-style: solid;
  border-width: 3px;
  border-color: #008800;
}
.background-img {
  z-index: -1;
  position: absolute;
  top: 0px;
  left: 0px;
  width: 100%;
  height: 100%;
  filter: blur(5px);
}
</style>