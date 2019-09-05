import Vue from 'vue'
import Vuex from 'vuex'
import { User } from '../api/user'
import {
    AUTH_REQUEST,
    AUTH_SUCCES,
    AUTH_ERROR,
    AUTH_LOGOUT,
    AUTH_BEGIN,
    SET_PHONE_NUMBER,
} from './mutation-types'
import axios from 'axios'

Vue.use(Vuex)

// export const store = new Vuex.store({
const state = {
    token: localStorage.getItem('user_token') || '',
    status: '',
    phone_number: ''
}

const getters = {
    is_authenticated: state => !!state.token, // return true, if LocalStorage don't empty
    auth_status: state => state.status,
    phone_number: state => state.phone_number
}


const mutations =  {
    [AUTH_REQUEST] (state) {
        state.status = 'loading'
    },
    [AUTH_SUCCES] (state) {
        state.status = 'succes'
    },
    [AUTH_ERROR] (state) {
        state.status = 'error'
    },
    [AUTH_BEGIN] (state) {
        state.status = 'begin' // sms succesfully sent
    },
    [AUTH_LOGOUT] (state) {
        state.status = undefined
    },
    [SET_PHONE_NUMBER] (state, phone_number) {
        state.phone_number = phone_number
    }
}
/* eslint-disable no-console */
const actions =  {
    get_sms (context, phone_number) {
        User.get_sms(phone_number).then(resp => {
            if (resp.Message == "Succes") {
                context.commit(AUTH_BEGIN)
            }
        })
    },
    confirm_phone (context, phone_number, otp) {
        User.confirm_phone(phone_number, otp).then(resp => {
            const token = resp.data.token
            localStorage.setItem('user-token', resp.data.token)
            axios.defaults.headers.common['Authorization'] = 'Bearer' + token
            context.commit(AUTH_SUCCES, {token})
            context.commit(SET_PHONE_NUMBER, phone_number)
        }).catch(err => {
            context.commit(AUTH_ERROR)
            localStorage.removeItem('user-token')
            return err
        })
    },
    logout (context) {
        return new Promise((resolve) => {
            context.commit(AUTH_LOGOUT)
            localStorage.removeItem('user-token')
            resolve()
        })
    }
}
export default new Vuex.Store({
    state,
    getters,
    mutations,
    actions
})