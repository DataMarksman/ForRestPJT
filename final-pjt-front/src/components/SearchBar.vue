<template>
  <div class="d-flex nav-bar-search-bar">
    <input
    class="inputbar hanna"
    placeholder="검색어를 입력해주세요."
    type="text" 
    v-model="keyword"
    @keyup.enter="searchResult(keyword)"
    >
    <div
    class="search-icon-container"
    @click="searchResult(keyword)"
    >
      <img class="search-icon" src="@/assets/search.png" alt="">
    </div>
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  data() {
    return {
      keyword: null,
      }
  },
  methods: {
    searchResult(keyword) {
      if (keyword.trim() !==''){
        this.$router.push({
          name: 'SearchView',
          params: {
            keyword: this.keyword,
          },
        });
        this.keyword = ''
        this.$store.state.searchResult = null
        this.$store.dispatch('getSearchResults', keyword)
        
      } else {
        alert('검색어를 입력해주세요.')
      }
    }
  }
}
</script>

<style>
@import url(//fonts.googleapis.com/earlyaccess/hanna.css);

.hanna * {
 font-family: 'Hanna', fantasy;
}
.inputbar{
  margin-top: 10px;
  width: 300px;
  height: 30px;
  font-size: 15px;
}
.nav-bar-search-bar {
  margin-top: 15px;
}
.search-icon {
  width: 33px;
}
.search-icon-container {
  margin-top: 11px;
  margin-left: 5px;
}
</style>