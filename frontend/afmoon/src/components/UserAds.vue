<template>
    <div class="container">
        <div class="row">
            <div class="d-flex justify-content-start col-12">
                <button @click="OnActive" :class="{ active: currentComponent === 'UserActiveAd' }">
                    Активные&nbsp;({{ is_active_count }})
                </button>
                <button @click="OnOld" :class="{ active: currentComponent === 'UserOldAd' }">
                    Завершенные&nbsp;({{ is_old_count }})
                </button>
            </div>
        </div>
        <div class="row">
            <div class="col-12">
                <componen v-bind:is="currentComponent" :active_ads="is_active" :old_ads="is_old">
                </componen>
            </div>
        </div>
    </div>
</template>

<script>
import { User } from '../api/user'
import UserActiveAd from './user/UserActiveAd'
import UserOldAd from './user/UserOldAd'
export default {
    name: 'UserAds',
    components: {
        UserActiveAd,
        UserOldAd
    },
    data(){
        return {
            currentComponent: 'UserActiveAd',
            ads: null,
            is_active: [],
            is_old: [],
        }
    },
    computed: {
        is_active_count(){
            return this.is_active.length
        },
        is_old_count(){
            return this.is_old.length
        }
    },
    methods: {
        OnActive(){
            this.currentComponent = 'UserActiveAd'
        },
        OnOld(){
            this.currentComponent = 'UserOldAd'
        },
        get_user_ad(){
            User.get_user_ad().then(response => {
                this.ads = response
                this.distribution_ads(this.ads.ad)
            })
        },
        distribution_ads(ads){
            for (let i = 0; i < ads.length; i++) {
                if (ads[i].is_active == true) {
                    this.is_active.push(ads[i])
                } else {
                    this.is_old.push(ads[i])
                }
            }
        }
    },
    beforeMount(){
        this.get_user_ad()
    }
}
</script>

<style>
button {
    border: none;
    display: block;
    padding: 3px 40px;
    font-size: 18px;
    margin: 0px 5px 0px 0px;
    background-color: white;
    border: 1px solid rgba(73,73, 73, 0.3);
    border-radius: 5px;
}
button.active {
    background-color: #e0e0e0;
}
</style>