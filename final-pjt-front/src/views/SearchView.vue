<template>
  <div>
    <div id="#">
      <div class="#">검색조건</div>
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

<style>
.border-line {
  border-style: solid;
  border-width: 3px;
  border-color: #008800;
}
</style>