<template>
    <div id="wrap">
        <div>
            <Add v-for="add in active_ads" v-bind:key="add.name" :add="add">
                <button class="btn" @click="activated_ad(add)">Снять Объявления</button>
                <button class="btn" @click="delete_ad(add)">Удалить</button>
                <router-link :to="'/edit/' + add.slug " class="btn">
                    Редактировать
                </router-link>
            </Add>
        </div>
    </div>
</template>

<script>
import { User } from '../../api/user'
import Add from '../Add'
export default {
    name: 'UserActiveAd',
    components: {
        Add
    },
    props: {
        active_ads: null
    },
    methods: {
        delete_ad(add){
            if (confirm("Вы действительно хотите удалить ?")){
                User.delete_ad(add.slug).then(response => {
                console.log(response)
                })
            }
        },
        activated_ad(add){
            if (confirm("Вы хотите снять объявления " + add.title + " ?")){
                User.active_ad(add.slug).then(response => {
                    console.log(response)
                })
            }
        }
    }
}
</script>

<style scoped>
.btn {
    border-radius: 5px;
    padding: 0px 7px;
    color: red;
    border: 1px solid red;
}
.btn:hover{
    background-color: red;
    color: white;
}
</style>