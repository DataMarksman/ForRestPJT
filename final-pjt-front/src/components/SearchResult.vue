<template>
   <div>
    <SearchResultItem
    v-for="SearchResult in getSearchResult"
    :key="SearchResult.id"
    :SearchResult="SearchResult"
    />
    <div class="loading-img" v-if="getSearchResult === null">
      <img  src="@/assets/loading_cute_img.gif" alt="">
      <p>검색 중입니다.</p>
    </div>
    
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
  created() {
    this.$store.dispatch('getSearchResults', this.keyword)
  }
}
</script>
<style>
<<<<<<< HEAD

=======
.img-box {
  width: 90%;
  margin-left: 50px;
  margin-right: 50px;
  display: flex;
  flex-wrap: wrap;
}
.loading-img{
  position: absolute;
  top: 35%;
  left: 40%;
  text-align: center;
}
>>>>>>> 7db050a02491d7e8409747b92a8d304e626f1f3b
</style>