<template>
    <div>
        <h1>ADD PRODUCT IN THEM SERVIC</h1>
        <ul>
            <li v-for="cat in cats" v-bind:key="cat.id">{{ cat.title }}</li>
        </ul>
    </div>
</template>

<script>
import { User } from '../api/user'
export default {
    name: 'AddProduct',
    computed: {
        categories () {
            return {}
        }
    },
    data () {
        return {
            cats: {}
        }
    },
    methods: {
        cat_level_1(){
            User.category().then(response => {
                this.cats = response
            })
        }
    },
    beforeMount (){
        this.cat_level_1()
    }
}
</script>

<style>

</style>