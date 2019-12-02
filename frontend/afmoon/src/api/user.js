/* eslint-disable no-console */
import { HTTP } from './common'

export const User = {
    get_sms (phone_number) {
        return HTTP.post('accounts/send-sms/', { 'phone_number': phone_number }).then(response => {
            return response
        })
    },
    confirm_phone (phone_number, otp, otp_key) {
        return HTTP.post('accounts/confirm-phone/', { 'phone_number': phone_number, 'otp': otp, 'otp_key': otp_key }).then(response => {
            console.log(response)
            return response
        })
    },
    profile () {
        return HTTP.get('accounts/profile/').then(response => {
            return response
        })
    },
    category (level=undefined, lft=undefined, rght=undefined) {
        return HTTP.get('category/', {
        params: {
            "level": level,
            "lft": lft,
            "rght": rght
        }}).then(response => {
                return response.data
            })
    },
    region (level=undefined, lft=undefined, rght=undefined) {
        return HTTP.get('region/', {
        params: {
            "level": level,
            "lft": lft,
            "rght": rght
        }}).then(response => {
                return response.data
            })
    },
    get_choices (choice){
        return  HTTP.get('choices/', {
            params: {
                "choices": choice
            }
        }).then(response => {
            return response.data
        })
    },
    add_ad(data){
        return HTTP.post('add-ad/', data).then(response => {
            console.log(response)
            return response
        })
    },
    user_detail(id){
        return  HTTP.get('user/' + String(id) + '/').then(response => {
            return response.data
        })
    },
    get_user_ad(){
        return HTTP.get('user-ads/').then(response => {
            return response.data
        })
    },
    get_edit_ad(slug){
        return HTTP.get('edit-ad/' + slug + '/').then(response => {
            return response.data
        })
    },
    put_ad(slug, data){
        return HTTP.put('edit-ad/' + slug + '/', data).then(response => {
            return response.data
        })
    },
    delete_ad(slug){
        return HTTP.delete('edit-ad/' + slug + '/').then(response => {
            return response.data
        })
    },
    active_ad(slug){
        return HTTP.put('edit-ad/active/' + slug + '/').then(response => {
            return response.data
        })
    }
}