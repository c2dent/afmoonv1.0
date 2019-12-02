/* eslint-disable no-console */
import axios from 'axios'

export const HTTP = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/'
})
axios.defaults.header = "Access-Control-Allow-Origin: *";

function add_token(){
    if (localStorage.getItem('user-token')) {
        HTTP.defaults.headers.common['Authorization'] = `Bearer ` + localStorage.getItem('user-token')
    }
}
add_token()