import { HTTP } from './common'

export const User = {
    get_sms () {
        return HTTP.get('accounts/send-sms/').then(response => {
            return response.data
        })
    },
    confirm_phone () {
        return HTTP.get('accounts/confirm-phone/').then(response => {
            return response.data
        })
    }
}