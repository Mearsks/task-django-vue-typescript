import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import Task from "@/views/Task.vue";
import Auth from '@/views/Auth.vue';

Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'Task',
    component: Task,
    meta: {
      title: 'Task',
    },
  },
  {
    path: '/auth',
    name: 'Auth',
    component: Auth,
    meta: {
      title: 'Auth',
    },
  },
]

const router = new VueRouter({
  routes
})

router.afterEach(to => {
  if (!to.meta.title) {
    return
  }
  document.title = to.meta.title
})

export default router
