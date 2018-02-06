<template>
  <div class="wrapper">
    <el-alert v-if="error"
              title="Something went wrong.."
              type="error">
    </el-alert>
    <h4>Risk Types <small>click to see more details</small></h4>
    <pulse-loader :loading="loading"></pulse-loader>
    <div v-for="item in items" class="item">
      <router-link :to="{name: 'list-detail' , params: {id: item.id} }">{{item.name}}</router-link>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'
  import {RISK_MANAGEMENT_API} from "@/services/api";
  import {PulseLoader} from 'vue-spinner/dist/vue-spinner.min.js'



  export default {
    name: 'app',
    data () {
      return {
        items: [],
        loading: true,
        error: false
      }
    },
    components: {
      PulseLoader
    },
    mounted(){
      this.loading = true
      axios.get(RISK_MANAGEMENT_API.list()).then(res => {
        this.items = res.data
        this.loading = false
      }).catch(err=>{
          this.loading = false
          this.error = true
      })
    }
  }
</script>

<style scoped>
  .wrapper{
    max-width: 700px;
    margin: auto ;
    padding: 0 10px;
  }
  .item{
    padding: 10px;
  }
</style>
