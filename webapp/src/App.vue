<template>
  <div id="app">
    <el-container>
      <el-header></el-header>
      <el-main class="main-wrapper">
        <router-view>
        </router-view>
      </el-main>
    </el-container>
  </div>
</template>


<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
  }

  h1, h2 {
    font-weight: normal;
  }
  body {
    margin: 0;
  }

  a {
    color: #42b983;
  }
  header{
    background-color:#42b983; ;
  }
  .main-wrapper {
    padding-top: 20px;
  }
</style>
