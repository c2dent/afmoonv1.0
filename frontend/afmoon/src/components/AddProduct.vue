<template>
    <div>
        <ChoiceCategory @OnChangeCategory="OnChangeCategory" @OnSelectCategory="OnSelectCategory"></ChoiceCategory>
        <form action="#" @submit.prevent="add_ad" enctype="multipart/form-data">
            <div>
                <BaseProduct v-if="baseproduct" @ChangeData="get_data"></BaseProduct>
                <Apartment v-if="apartment" @ChangeData="get_data"></Apartment>
                <Avtomobil v-if="avtomobil" @ChangeData="get_data"></Avtomobil>
                <House v-if="house" @ChangeData="get_data"></House>
                <Land v-if="land" @ChangeData="get_data"></Land>
                <Vacancy v-if="vacancy" @ChangeData="get_data"></Vacancy>
                <Resume v-if="resume" @ChangeData="get_data"></Resume>
                <Second v-if="second" @ChangeData="get_data"></Second>
                <PersonalsClothes v-if="personalsclothes" @ChangeData="get_data"></PersonalsClothes>
                <PersonalsShoes v-if="personalsshoes" @ChangeData="get_data"></PersonalsShoes>
            </div>
            <ChoiceRegion v-if="category_select" @OnSelect="OnSelectRegion"></ChoiceRegion>
            <div class="d-flex heading" v-if="category_select">
                <h4>Контакты</h4>
            </div>
            <div class="d-flex" v-if="category_select">
                <button class="btn btn-outline-success h35" type="submit">Опубликовать</button>
            </div>
        </form>
    </div>
</template>

<script>
import store from '../store/index'
import BaseProduct from './ProductModel/BaseProduct'
import Apartment from './ProductModel/Apartment'
import Avtomobil from './ProductModel/Avtomobil'
import House from './ProductModel/House'
import Land from './ProductModel/Land'
import Vacancy from './ProductModel/Vacancy'
import Resume from './ProductModel/Resume'
import Second from './ProductModel/Second'
import PersonalsClothes from './ProductModel/PersonalsClothes'
import PersonalsShoes from './ProductModel/PersonalsShoes'
import ChoiceCategory from './ProductModel/ChoiceCategory'
import ChoiceRegion from './ProductModel/ChoiceRegion'
export default {
    name: 'AddProduct',
    components : {
        BaseProduct,
        Apartment,
        Avtomobil,
        House,
        Land,
        Vacancy,
        Resume,
        Second,
        PersonalsClothes,
        PersonalsShoes,
        ChoiceCategory,
        ChoiceRegion,
    },
    data () {
        return {
            baseproduct: false,
            apartment: false,
            avtomobil: false,
            house: false,
            land:false,
            vacancy:false,
            resume: false,
            second: false,
            personalsclothes:false,
            personalsshoes: false,
            category_select : false,
            region:'',
            category:'',
            data:{}
        }
    },
    computed: {
        get_profile(){
            return store.getters.get_profile
        }
    },
    methods: {
        OnSelectCategory(elm){
            this.hidden_content()
            if (elm.id == 172) {
                this.avtomobil = true
            } else if (elm.id == 169) {
                this.apartment = true
            } else if (elm.id == 170) {
                this.house = true
            } else if (elm.id == 167) {
                this.vacancy = true
            } else if (elm.id == 168) {
                this.resume = true
            } else if (elm.id == 148 || elm.id == 149 || elm.id == 150 || elm.id == 151) {
                this.second = true
            } else {
                this.baseproduct = true
            }
            this.category = elm
            this.category_select = true
        },
        OnChangeCategory(){
            this.category_select = false
            this.hidden_content()
            this.category = ''
        },
        OnSelectRegion(elm){
            this.region = elm
        },
        OnChangeRegion(){
            this.region = ''
        },
        get_data(data){
            this.data = data
        },
        add_ad(){
            this.data.append('category', this.category.id);
            this.data.append('region', this.region.id);
            this.data.append('user',this.get_profile.id)
            store.dispatch('add_ad', this.data)
        },
        hidden_content() {
            this.baseproduct = false,
            this.apartment = false,
            this.avtomobil = false,
            this.house = false,
            this.land = false,
            this.second = false,
            this.vacancy = false,
            this.resume = false,
            this.personalsclothes = false,
            this.personalsshoes = false
        }

    },
    beforeMount (){
    }
}
</script>

<style>
.heading {
    margin: 25px 0px;
    font-weight: 600;
}
.h35 {
	height:31px;
	padding:0px 7px;
}
</style>