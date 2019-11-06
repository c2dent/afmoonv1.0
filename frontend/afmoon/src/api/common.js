/* eslint-disable no-console */
import axios from 'axios'

export const HTTP = axios.create({
    baseURL :'http://127.0.0.1:8000/api/',
    headers: {
        'Authorization': `Bearer ${localStorage.getItem('user-token')}`
    }
})
axios.defaults.header = "Access-Control-Allow-Origin: *";
// headers: {
//     'Authorization': `Bearer ${localStorage.getItem('user-token')}`
// }