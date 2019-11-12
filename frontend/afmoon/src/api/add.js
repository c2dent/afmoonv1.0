/* eslint-disable no-console */
import { HTTP } from './common'

export const Get_Add = {
    by_region(region){
        return HTTP.get(region + '/').then(response => {
            return response.data
        })
    }
}