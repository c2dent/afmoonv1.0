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
    SET_PROFILE,
} from './mutation-types'
import axios from 'axios'

Vue.use(Vuex)

// export const store = new Vuex.store({
const state = {
    token: localStorage.getItem('user_token') || '',
    status: '',
    phone_number: '',
    profile: {}
}

const getters = {
    is_authenticated: state => !!state.token, // return true, if LocalStorage don't empty
    auth_status: state => state.status,
    phone_number: state => state.phone_number,
    get_profile: state => state.profile
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
    },
    [SET_PROFILE] (state, profile){
        state.profile = profile
    }
}
/* eslint-disable no-console */
const actions =  {
    get_sms (context, data) {
        return new Promise((resolve) => {
            User.get_sms(data.phone_number).then(resp => {
                if (resp.data.Status == 'Success') {
                    localStorage.setItem('otp_key', resp.data.Details)
                    context.commit(SET_PHONE_NUMBER, data.phone_number)
                    context.commit(AUTH_BEGIN)
                }
                resolve()
            })
        })
    },
    confirm_phone (context, data) {
        User.confirm_phone(data.phone_number, data.otp, data.otp_key).then(resp => {
            console.log(resp)
            const token = resp.data.token
            localStorage.setItem('user-token', token)
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + token
            context.commit(AUTH_SUCCES, {token})
            context.commit(SET_PHONE_NUMBER, data.phone_number)
            location.reload()
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
    },
    get_profile (context) {
        User.profile().then(resp => {
            if (resp.status == 200) {
                context.commit(SET_PROFILE, resp.data)
            }
        })
    }
}
export default new Vuex.Store({
    state,
    getters,
    mutations,
    actions
})