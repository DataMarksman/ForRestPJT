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
    popularMovies: null,
    searchResult: [],
    movieDetail: null,
    movieCommentList: null,
    movieComment: null,
    topRatedMovies: null,
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
    },
    GET_COMMENT_LIST(state, comments) {
      state.movieCommentList = comments
    },
    GET_COMMENT_DETAIL(state, comment) {
      state.movieComment = comment
    },
    GET_MOVIE_DETAIL(state, movie) {
      state.movieDetail = movie
    },
    GET_POPULAR_MOVIES(state, movies) {
      state.popularMovies = movies
    },
    GET_TOP_RATED_MOVIES(state, movies) {
      state.topRatedMovies = movies
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
    getCurrentMovieList(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/newmovie/`,
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
        url: `${API_URL}/movies/search/${keyword}`,
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
          res
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
    },
    addComment(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/movies/${payload.movie_id}/comments/create/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        },
        data: {
          content: payload.commentContent
        }
      })
        .then((res) => {
          context.dispatch('getCommentList', payload.movie_id)
          res
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getCommentList(context, movie_id) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/${movie_id}/comments/`,
      })
        .then((res) => {
          context.commit('GET_COMMENT_LIST', res.data)
        })
    },
    sendLikeInfo(context, movie_id) {
      axios({
        method: 'post',
        url: `${API_URL}/movies/${movie_id}/like/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        },
      })
        .then((res) => {
          context.dispatch('getMovieDetail', movie_id)
          res
        })
        .then((err) => {
          console.log(err)
        })
    },
    getMovieDetail(context, movie_id) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/${movie_id}`
      })
        .then((res) => {
          context.commit('GET_MOVIE_DETAIL', res.data)
          console.log(res.data)
        })
        .catch((err) => {
        console.log(err)
        })
    },
    // getCommentDetail(context, payload) {
    //   axios({
    //     method: 'get',
    //     url: `${API_URL}/movies/${payload.movie_id}/comments/${payload.comment_id}/`,
    //     headers: {
    //       Authorization: `Token ${context.state.token}`
    //     },
    //   })
    //     .then((res) => {
    //       context.commit('GET_COMMENT_DETAIL', res.data)
    //       console.log('단일 댓글까진 옴')
    //     })
    //     .catch((err) => {
    //       console.log(err)
    //     })
      
    // },
    sendCommentAdjust(context, payload) {
      axios({
        method: 'put',
        url: `${API_URL}/movies/${payload.movie_id}/comments/${payload.comment_id}/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        },
        data: {
          content: payload.content,
        }
      })
        .then((res) => {
          context.dispatch('getCommentList', payload.movie_id)
          res
        })
        .catch((err) => {
          console.log(err)
        })
    },
    commentDelete(context, payload) {
      axios({
        method: 'delete',
        url: `${API_URL}/movies/${payload.movie_id}/comments/${payload.comment_id}/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        },
      })
        .then((res) => {
          context.dispatch('getCommentList', payload.movie_id)
          res
        })
        .catch((err) => {
          console.log(err)
        })
    },
    commentLike(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/movies/${payload.movie_id}/comments/${payload.comment_id}/like/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        },
      })
        .then((res)=> {
          context.dispatch('getCommentList', payload.movie_id)
          res
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getPopularMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/popular`
      })
        .then((res) => {
          context.commit('GET_POPULAR_MOVIES',res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getTopRatedMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/toprated/`
      })
        .then((res) => {
          context.commit('GET_TOP_RATED_MOVIES',res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    }

    
  },
  modules: {
  
  }
})
