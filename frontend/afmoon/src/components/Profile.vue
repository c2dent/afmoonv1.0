<template>
    <div id="Wrap" class="container mt-4">
        <div class="row pt-5">
            <div class="col-3 d-flex flex-column justify-content-center align-items-center">
                <div>
                    <img :src="'http://127.0.0.1:8000' + profile.avatar" alt="">
                </div>
                <div>
                    <p class="pt-4">{{ profile.nickname }}</p>
                </div>
                <div>
                    <p class="pt-1">место: {{ profile.region }}</p>
                </div>
                <div id="user-nav" class="d-flex flex-column">
                    <router-link to="/profile/settings">Настройки</router-link>
                    <router-link to="/profile/ads">Мои объявлении</router-link>
                    <router-link to="/add-product">Подать объявление</router-link>
                    <button class="btn btn-outline-danger mt-3 h31">Выйти</button>
                </div>
            </div>
            <div class="col-9">
                <router-view></router-view>
            </div>
        </div>
    </div>
</template>
<script>
import store from '../store/index'

export default {
    name: 'Profile',
    computed: {
        profile () {
            return store.getters.get_profile
        }
    },
}
</script>

<style scoped>
img {
    max-width: 100px !important;
    max-height: auto !important;
}
#Wrap {
    border-top: 1px solid rgba(73,73, 73, 0.1);
}
router-link {
    display: block;
    margin: 2px;
    padding: 5px;
}
.h31 {
    max-height: 31px;
    padding:0px 7px;
}
#user-nav {
    border-top: 1px solid rgba(73,73, 73, 0.3);
    padding: 15px 5px;
}
</style>