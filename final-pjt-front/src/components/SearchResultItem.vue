<template>
  
    <div @click="toDetailpage" class="col-2 img-card-box">
      <div class="img-content">
        <img class="img" :src="SearchResult.poster_path" alt="">
      </div>
      
      <div>
        {{ SearchResult.title }}
      </div>
    </div>
  
</template>

<script>
export default {
  name: 'SearchResultItem',
  props: {
    SearchResult : Object
  },
  methods: {
    toDetailpage() {
      const SearchResult = this.SearchResult
      this.$router.push({name: 'DetailView', params: { id: SearchResult.tmdb_id}})
    }
  }
}
</script>

<style scoped>
.img {
  width: 80%;
  height: auto;
  border: 2px solid rgb(130, 127, 127);
}
.img-card-box{
  position: relative;
  
}
.img-container {
  
}
.img-content {
  cursor: pointer;
}
</style>