import Vue from 'vue'
import VueRouter from 'vue-router'
import Profile from '../components/Profile'
import UserSettings from '../components/UserSettings'
import UserAds from '../components/UserAds'

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
    ]
})