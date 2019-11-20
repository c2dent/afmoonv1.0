import Vue from 'vue'
import VueRouter from 'vue-router'
import Profile from '../components/Profile'
import UserSettings from '../components/UserSettings'
import UserAds from '../components/UserAds'
import AddProduct from '../components/AddProduct'
import AddList from '../components/AddList'
import ProductDetail from '../components/ProductDetail'

Vue.use(VueRouter)

export default new VueRouter({
    routes : [
        {
            path: '/profile/',
            component: Profile,
            children: [
                {
                    path: 'settings/',
                    component: UserSettings
                },
                {
                    path: 'ads/',
                    component: UserAds
                },
            ]
        },
        {
            path: '/add-product',
            component: AddProduct
        },
        {
            path:'/:region',
            component: AddList
        },
        {
            path:'/:region/:category',
            component: AddList
        },
        {
            path:'/:region/:category/:slug',
            component: ProductDetail
        }
    ]
})