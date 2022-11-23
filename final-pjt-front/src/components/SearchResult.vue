<template>
  
  <div class="img-box">
    <SearchResultItem
    v-for="SearchResult in getSearchResult"
    :key="SearchResult.id"
    :SearchResult="SearchResult"
    />
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
  display: flex;
  flex-wrap: wrap;
}
</style>