import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'
Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    token: null,
    currentBroadMovies: []
    
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
      GET_MOVIE_LIST(state, currentBroadMovies) {
        state.currentBroadMovies = currentBroadMovies
      },
      SAVE_TOKEN(state, token) {
        state.token = token
        router.push({ name: 'ArticleView' })
      },
    },

  
  actions: {
    signUp(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username: payload.username,
          password1: payload.password1,
          password2: payload.password2,
        }
      })
        .then((res) => {
          // console.log(res)
          context.commit('SAVE_TOKEN', res.data.key)
        })
    },
    logIn(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username: payload.username,
          password: payload.password,
        }
      })
        .then((res) => {
          console.log(res)
          context.commit('SAVE_TOKEN', res.data.key)
        })
    },
    getMovieList(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/`,
        // headers: {
        //   Authorization: `Token ${context.state.token}`
        // }
      })
        .then((res) => {
          
          context.commit('GET_MOVIE_LIST', res.data)
        })
        .catch((err) =>{
          console.log(err)
        }
        )
    },
  },
  modules: {
  
  }
})
