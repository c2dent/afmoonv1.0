<template>
    <div>
        <div class="d-flex">
            <h4 v-if="ad">
                Категория:&nbsp;&nbsp;{{ ad.category_title }}
            </h4>
        </div>
        <form action="#" @submit.prevent="save_change" enctype="multipart/form-data">
            <div>
                <componen v-bind:is="current_component" :default_data="ad" @ChangeData="get_data"></componen>
            </div>
            <div class="d-flex mt-4 mb-4" v-if="ad">
                <h4>Место встречи:&nbsp;&nbsp;{{ ad.region_title }}</h4>
            </div>
            <div class="d-flex mb-3">
                <h4>Контакты</h4>
            </div>
            <div class="container">
                <div class="row">
                    <div class="col-2 d-flex">
                        Тел номер
                    </div>
                    <div class="col-8 d-flex">
                        {{ get_profile.phone_number }}
                    </div>
                    <div class="col-2">

                    </div>
                </div>
            </div>
            <div class="d-flex wrap_submit">
                <button class="btn-outline-success btn h35" type="submit">Сохранить изменения</button>
            </div>
        </form>
        {{ad}}
    </div>
</template>

<script>
import store from '../../store/index'
import { User } from '../../api/user'
import EditBaseProduct from './EditBaseProduct.vue'
import EditApartment from './EditApartment.vue'
import EditAvtomobil from './EditAvtomobil.vue'
import EditHouse from './EditHouse.vue'
import EditResume from './EditResume.vue'
import EditLand from './EditLand.vue'
import EditVacancy from './EditVacancy.vue'
import EditPersonalsShoes from './EditPersonalsShoes.vue'
import EditPersonalsClothes from './EditPersonalsClothes.vue'
export default {
    name: 'EditAd',
    components: {
        EditBaseProduct ,
        EditApartment,
        EditAvtomobil,
        EditHouse,
        EditLand,
        EditResume,
        EditVacancy,
        EditPersonalsShoes,
        EditPersonalsClothes
    },
    data(){
        return {
            ad: null,
            data: {},
        }
    },
    computed: {
        slug: function(){
            return this.$route.params.slug
        },
        get_profile(){
            return store.getters.get_profile
        },
        current_component: function(){
            let component = ''
            if (this.ad){
                let category = this.ad.category
                if (category == 172){
                    component = 'EditAvtomobil'
                } else if (category == 169) {
                    component = 'EditApartment'
                } else if (category == 170) {
                    component = 'EditHouse'
                } else if (category == 171){
                    component = 'EditLand'
                } else if (category == 167){
                    component = 'EditVacancy'
                } else if (category == 168){
                    component = 'EditResume'
                } else if (category == 1134){
                    component = 'EditSecond'
                } else {
                    component = 'EditBaseProduct'
                }
            }
            return component
        }
    },
    methods: {
        get_edit_ad(){
            User.get_edit_ad(this.slug).then(response => {
                this.ad = response
            })
        },
        save_change(){
            this.data.append('category', this.ad.category);
            this.data.append('region', this.ad.region);
            this.data.append('user',this.ad.user);
            User.put_ad(this.slug, this.data).then(response => {
                console.log(response)
            })
        },
        get_data(data){
            this.data = data
        },
    },
    beforeMount(){
        this.get_edit_ad()
    }
}
</script>

<style>
.h35 {
	height: 31px;
	padding: 0px 7px;
}
.wrap_submit {
    margin: 15px 0px 10px 0px;
}
</style>