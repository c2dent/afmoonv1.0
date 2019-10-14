<template>
    <div>
        <ChoiceCategory @OnChange="OnChangeCategory" @OnSelect="OnSelectCategory"></ChoiceCategory>
        <div>
            <PersonalsShoes v-if="category_select"></PersonalsShoes>
        </div>
        <ChoiceRegion v-if="category_select"></ChoiceRegion>
        <div class="d-flex heading" v-if="category_select">
            <h4>Контакты</h4>
        </div>
        <div class="d-flex" v-if="category_select">
            <button class="btn btn-outline-success h35">Опубликовать</button>
        </div>
    </div>
</template>

<script>
import { User } from '../api/user'
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
            category_select : false,
        }
    },
    methods: {
        OnSelectCategory(){
            this.category_select = true
        },
        OnChangeCategory(){
            this.category_select = false
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