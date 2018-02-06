import Vue from 'vue'
import Router from 'vue-router'
import List from '@/components/list.vue'
import ListDetail from '@/components/list-detail.vue'

Vue.use(Router)
export default new Router({
  // mode: 'history',
  routes: [
    {
      path: '/',
      components: {
        default: List,
      }
    },
    {
      name : 'list-detail',
      path: '/list-detail/:id',
      components: {
        default: ListDetail,
      },
    },
    {
      path: '*',
      redirect : '/'
    }
  ]
})
