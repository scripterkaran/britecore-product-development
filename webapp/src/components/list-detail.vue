<template>
  <div class="form-wrapper">
    <pulse-loader :loading="loading"></pulse-loader>
    <el-alert v-if="error"
              title="Something went wrong.."
              type="error">
    </el-alert>
    <el-form label-position="right" label-width="220px">
      <el-form-item label="Risk Type Name">
        <el-input :value="item.name"></el-input>
      </el-form-item>
      <el-form-item v-for="field in item.fields" :label="field.label" :key="field.id">
        <div v-if="field.type == 'number'" class="fix">
          <el-input-number v-model="field.value"></el-input-number>
        </div>
        <div v-if="field.type == 'text'">
          <el-input type="text" v-model="field.value"></el-input>
        </div>
        <div v-if="field.type == 'date'">
          <el-date-picker v-model="field.value"></el-date-picker>
        </div>
        <div v-if="field.type == 'enum'">
          <el-select v-model="field.value" placeholder="Select" class="el-select">
            <el-option v-for="option in field.meta.options" :value="option" :key="option"
                       :label="option"></el-option>
          </el-select>
        </div>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
  import axios from 'axios'
  import {RISK_MANAGEMENT_API} from "@/services/api";
  import {PulseLoader} from 'vue-spinner/dist/vue-spinner.min.js'

  export  default {
    data (){
      return {
        item: {},
        loading: true,
        error: false
      }
    },
    components: {
      PulseLoader
    },
    mounted(){
      this.fetch()
    },
    watch: {
      '$route.params'() {
        this.fetch()
      }
    },
    methods: {
      fetch(){
        let params = this.$route.params.id
        this.loading = true
        axios.get(RISK_MANAGEMENT_API.get(params)).then(res => {
          this.item = res.data
          this.loading = false
        }).catch(err => {
          this.loading = false
          this.error = true
        })
      },
      parseOptions(meta){
          console.log(meta)
        if (meta.options){
          return JSON.parse(meta.options)
        }
        return []
     }
    },

  }
</script>
<style scoped lang="scss">


  .form-wrapper {
    max-width: 700px;
    margin: auto;
  }

  select {
    width: 100%;
    padding: 16px 20px;
    border: none;
    border-radius: 4px;
    background-color: #f1f1f1;
  }

  input {
    width: 100%;
    padding: 12px 20px;
    margin: 8px 0;
    box-sizing: border-box;
  }

  .form-wrapper label {
    margin-bottom: 10px;
    display: inline-block;
  }

  .el-select {
    width: 100%;

  }

  .input-field {
    margin-bottom: 10px;
  }

  .fix /deep/ .el-input-number__increase {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 38px;
  }

  .fix /deep/ .el-input-number__decrease {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 38px;
  }
</style>
