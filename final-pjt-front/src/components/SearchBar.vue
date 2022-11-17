<template>
  <div class="right">
    <input
    class="inputbar"
    placeholder="검색어를 입력해주세요."
    type="text" 
    v-model="keyword"
    @keyup.enter="searchResult(keyword)"
    >
    <button
    @click="searchResult(keyword)"
    >입력</button>
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
            isResultShow: true,
          },
        });
        this.keyword = ''
        console.log('"', keyword, '"'+ '검색')
      } else {
        alert('검색어를 입력해주세요.')
      }
    }
  }
}
</script>

<style>
.right{
  float:right;
}
.inputbar{
  width: 300px;
  height: 30px;
  font-size: 25px;
}
</style>