import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  state: {
    token: null,
    currentBroadMovies: []
    
  },
  getters: {
  },
  mutations: {
      GET_MOVIE_LIST(state, currentBroadMovies) {
        state.currentBroadMovies = currentBroadMovies
      }
    },

  
  actions: {
    signUp() {
      console.log('signUp완료')
    },
    logIn() {
      console.log('login 완료!')
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
          console.log('영화 데이터 받기 완료')
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
