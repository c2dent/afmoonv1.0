<template>
    <div id="wrap">
        <div>
            <Add v-for="add in old_ads" v-bind:key="add.name" :add="add">
                <button class="btn_green" @click="activated_ad(add)">Опубликовать</button>
                <button class="btn" @click="delete_ad(add)">Удалить</button>
                <router-link :to="'/edit/' + add.slug " class="btn">
                    Редактировать
                </router-link>
            </Add>
        </div>
    </div>
</template>

<script>
import Add from '../Add'
import { User } from '../../api/user'
export default {
    name: 'UserOldAd',
    components: {
        Add,
    },
    props: {
        old_ads: null,
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
            if (confirm("Вы хотите активировать Объявления ?")){
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
.btn_green {
    border-radius: 5px;
    padding: 0px 7px;
    color: #28a745;
    border: 1px solid #28a745;
}
.btn_green:hover {
    background-color: #28a745;
    color:white;
}
</style>