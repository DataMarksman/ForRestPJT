<template>
  <div>
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

.inputbar{
  margin-top: 10px;
  width: 300px;
  height: 30px;
  font-size: 15px;
}
</style>