import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/LoginView'
import SignupView from '@/views/SignupView'
import SearchView from '@/views/SearchView'
import UserProfileView from '@/views/UserProfileView'
import DetailView from '@/views/DetailView'
import ProfileEditView from '@/views/ProfileEditView'
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
    path: '/profile',
    name: 'UserProfileView',
    component: UserProfileView
  },
  {
    path: '/:id',
    name: 'DetailView',
    component: DetailView
  },
  {
    path: '/profileEdit',
    name: 'ProfileEditView',
    component: ProfileEditView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
