/* eslint-disable no-console */
import { HTTP } from './common'

export const User = {
    get_sms (phone_number) {
        return HTTP.post('accounts/send-sms/', { 'phone_number': phone_number }).then(response => {
            console.log(response.data)
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
            console.log(response)
            return response
        })
    }
}