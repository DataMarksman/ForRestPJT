<template>
  
  <div class="img-box">
    <SearchResultItem
    v-for="SearchResult in getSearchResult"
    :key="SearchResult.id"
    :SearchResult="SearchResult"
    />
    <p v-if="getSearchResult === null"> 검색 중 입니다.</p>
  </div>
 
</template>

<script>
import SearchResultItem from '@/components/SearchResultItem'
export default {
  name:'SearchResult',
  props: {
    keyword: String,
  },
  components: {
    SearchResultItem
  },
  computed: {
    getSearchResult() {
      return this.$store.state.searchResult
    }
  },
  // created() {
  //   this.$store.dispatch('getSearchResults', this.keyword)
  // }
}
</script>

<style>
.img-box {
  width: 90%;
  margin-left: 50px;
  margin-right: 50px;
  display: flex;
  flex-wrap: wrap;
}
</style>