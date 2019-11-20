/* eslint-disable no-console */
import { HTTP } from './common'

export const Get_Add = {
    by_region(region){
        return HTTP.get(region + '/').then(response => {
            return response.data
        })
    },
    by_region_category(region, category){
        return HTTP.get(region + '/' + category + '/').then(response => {
            return response.data
        })
    },
    add_detail(region,category, slug){
        return HTTP.get(region + '/' + category + '/' + slug + '/').then(response => {
            return response.data
        })
    }
}