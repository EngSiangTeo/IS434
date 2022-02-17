import { createRouter, createWebHistory } from 'vue-router'
import Network from '../views/Network.vue'
import Async from '../views/Async.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [{
    path: '/',
    name: 'Home',
    component: Network,
  },
  {
    path: '/async',
    name: 'Async',
    component: Async,
  }]
})

export default router