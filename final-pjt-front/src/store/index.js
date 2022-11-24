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
    currentUser: null,
    token: null,
    currentBroadMovies: [],
    searchResult: [],
    
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    GET_USER_INFO(state, user) {
      state.currentUser = user
    },
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({ name: 'HomeView' })
    },
    GET_MOVIE_LIST(state, currentBroadMovies) {
        state.currentBroadMovies = currentBroadMovies
    },
    // GET_MOVIE_SEARCH(state, searchMovieList) {
    //   state.searchMovieList = searchMovieList
    // },
    GET_SEARCH_RESULT(state, searchResult) {
      state.searchResult = searchResult
    },
    LOG_OUT(state) {
      state.token = null
      state.currentUser = null
      router.push({ name: 'HomeView'})
    }
  },

  
  actions: {
    getUserInfo(context) {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then((res) => {
          console.log(res)
          context.commit('GET_USER_INFO', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
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
          context.dispatch('getUserInfo')
        })
        .catch((err) => {
          alert('올바르지 않은 형식입니다.')
          console.log(err)
        }
        )
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
          context.dispatch('getUserInfo')
        })
        .catch((err)=> {
          alert('아이디 혹은 비밀번호가 맞지 않습니다.')
          console.log(err)
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
    getSearchResults(context, keyword) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/`,
        params: {
          keyword: keyword
        }
      })
        .then((res) => {
          context.commit('GET_SEARCH_RESULT', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    changeLike(context, movie_pk) {
      axios({
        method: 'post',
        url: `${API_URL}/${movie_pk}/like/`,
      })
        .then((res) => {
          console.log(res)
          context.commit('CHANGE_LIKE', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    logOut(context) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`,
        
      })
        .then((res) => {
          res
          context.commit('LOG_OUT')
        })
        .catch((err) => {
          console.log(err)
        })
    }
    
  },
  modules: {
  
  }
})
