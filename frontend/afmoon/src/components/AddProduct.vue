<template>
    <div>
        <h3>Выберите категории</h3>
        <div class="select">
            <FormSelect :categories="cats_level_1" @cat_up="level_1" class="form_select"></FormSelect>
            <FormSelect :categories="cats_level_2" v-if="element_level_2" @cat_up="level_2" class="form_select"></FormSelect>
            <FormSelect :categories="cats_level_3" v-if="element_level_3" @cat_up="level_3" class="form_select"></FormSelect>
            <FormSelect :categories="cats_level_4" v-if="element_level_4" class="form_select"></FormSelect>
        </div>
        <h3>Параметры</h3>
        <div>
            <BaseProduct></BaseProduct>
        </div>
    </div>
</template>

<script>
import FormSelect from './costom_elements/FormSelect'
import { User } from '../api/user'
import BaseProduct from './ProductModel/BaseProduct'
export default {
    name: 'AddProduct',
    components : {
        FormSelect,
        BaseProduct,
    },
    data () {
        return {
            cats_level_1: {},
            cats_level_2: {},
            cats_level_3: {},
            cats_level_4: {},
            element_level_2 : false,
            element_level_3 : false,
            element_level_4 : false,
        }
    },
    methods: {
        get_categories(level){
            User.category(level).then(response => {
                this.cats_level_1 = response
            })
        },
        level_1(cat){
            this.element_level_2 = false
            this.element_level_3 = false
            this.element_level_4 = false
            if ((cat.rght - cat.lft) > 1 ) {
                this.element_level_2 = true
                User.category(cat.level+1, cat.lft, cat.rght).then( response => {
                    this.cats_level_2 = response
                })
            }
        },
        level_2(cat){
            this.element_level_3 = false
            this.element_level_4 = false
            if ((cat.rght - cat.lft) > 1) {
                this.element_level_3 = true
                User.category(cat.level+1, cat.lft, cat.rght).then(response => {
                    this.cats_level_3 = response
                })
            }
        },
        level_3(cat){
            this.element_level_4 = false
            if((cat.rght - cat.lft) > 1){
                this.element_level_4 = true
                User.category(cat.level + 1, cat.lft, cat.rght).then(response => {
                    this.cats_level_4 = response
                })
            }
        }
    },
    beforeMount (){
        this.get_categories('1')
    }
}
</script>

<style>
.select {
    display: flex;
    flex-wrap: wrap;
}
.form_select {
    margin: 3px;
}
</style>