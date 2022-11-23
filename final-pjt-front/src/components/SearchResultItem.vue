<template>
  
    <div class="col-4">
      <div class="img-container">
        <div class="img-content">
          <img :src="SearchResult.poster_path" alt="">
        </div>
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
  }
}
</script>

<style>
.img-card-box{
  width: 90%;
  margin-left: 15px;
}
.img-container {
  width: 100px;
}
.img-content {
  width: 90%
}
</style>