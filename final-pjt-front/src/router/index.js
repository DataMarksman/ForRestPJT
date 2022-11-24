import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/LoginView'
import SignupView from '@/views/SignupView'
import SearchView from '@/views/SearchView'
import UserProfileView from '@/views/UserProfileView'
import DetailView from '@/views/DetailView'

Vue.use(VueRouter)


const routes = [
  {
    path:'/',
    name: 'HomeView',
    component: HomeView
  },
  {
    path:'/login',
    name:'LoginView',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'SignupView',
    component: SignupView
  },
  {
    path: '/search/:keyword',
    name: 'SearchView',
    component: SearchView
  },
  {
    path: '/profile/:id',
    name: 'UserProfileView',
    component: UserProfileView
  },
  {
    path: '/:id',
    name: 'DetailView',
    component: DetailView,
    params: true
  },
  // {
  //   path: '/404',
  //   name: 'NOT_FOUND_404',
  //   component: NotFoundView
  // },
  // {
  //   path: '*',
  //   component:
  // }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
