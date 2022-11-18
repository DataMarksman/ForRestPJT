import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    userInfo: {
      showComment: true,
      showFollow: false,
      showFollowing: false,
      showLikeMovie: false,
      showScoreRate: false,
    },
  },
  getters: {
  },
  mutations: {
    TO_LIKE_PAGE(state) {
      state.userInfo = {
        showComment: true,
        showFollow: false,
        showFollowing: false,
        showLikeMovie: false,
        showScoreRate: false
      }
     
    },
    TO_FOLLOW_PAGE(state) {
      state.userInfo = {
        showComment: false,
        showFollow: true,
        showFollowing: false,
        showLikeMovie: false,
        showScoreRate: false
      }
    },
    TO_FOLLOWING_PAGE(state) {
      state.userInfo = {
        showComment: false,
        showFollow: false,
        showFollowing: true,
        showLikeMovie: false,
        showScoreRate: false
      }
    },
    TO_COMMENT_PAGE(state) {
      state.userInfo = {
        showComment: false,
        showFollow: false,
        showFollowing: false,
        showLikeMovie: true,
        showScoreRate: false
      }
    },
    TO_SCORERATE_PAGE (state) {
      state.userInfo = {
        showComment: false,
        showFollow: false,
        showFollowing: false,
        showLikeMovie: false,
        showScoreRate: true
      }
    },

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
