/* eslint-disable no-console */
import { HTTP } from './common'

export const User = {
    get_sms (phone_number) {
        return HTTP.post('accounts/send-sms/', { 'phone_number': phone_number }).then(response => {
            console.log(response)
            return response.data
        })
    },
    confirm_phone (phone_number, otp) {
        return HTTP.post('accounts/confirm-phone/', { 'phone_number': phone_number, 'otp': otp }).then(response => {
            return response.data
        })
    }
}