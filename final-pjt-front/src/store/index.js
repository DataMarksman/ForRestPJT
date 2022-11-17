import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
    signUp() {
      console.log('signUp완료')
    },
    logIn() {
      console.log('login 완료!')
    }
  },
  modules: {
  }
})
