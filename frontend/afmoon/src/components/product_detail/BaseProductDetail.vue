<template>
    <div id="wrap">
        <div class="container">
            <div class="row">
                <div class="col-8">
                    <div class="container">
                        <div class="row">
                            <div class="title col-8">
                                <h3>
                                    {{ add.title }}
                                </h3>
                            </div>
                            <div class="chosen col-4">
                                <p>Добавить избранное</p>
                            </div>
                        </div>
                        <div class="row">
                            <div class="carousel">
                                <div class="wrap_main_img">
                                    <img :src="'http://127.0.0.1:8000' + main_img" alt="" ref="image" :class="{img_land:main_img_land, img_portait:main_img_portrait}" @load="load_main_img">
                                </div>
                                <div class="wrap_choice_img">
                                    <div class="choice_img">
                                        <div v-for="image in add.images" v-bind:key="image.image" class="wrap_images">
                                            <img :src="'http://127.0.0.1:8000' + image.image" alt="" @click="click_img($event)">
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-12 p-0 m-0">
                                <slot v-bind:add="add">
                                </slot>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-12 wrap_description m-0 p-0">
                                <div class="description d-flex justify-content-start">
                                    <p>
                                        <b>
                                            {{ add.description }}
                                        </b>
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-4">
                    <div class="container">
                        <div class="row">
                            <div class="wrap_card_user col-12">
                                <div class="card">
                                    <div class="avatar">
                                        <router-link :to="'/user/' + add.user">
                                            <img :src="'http://127.0.0.1:8000' + add.user_avatar" alt="">
                                        </router-link>
                                    </div>
                                    <div class="nickname">
                                        <h5>
                                            <router-link to="">
                                                {{ add.user_nickname }}
                                            </router-link>
                                        </h5>
                                    </div>
                                    <div class="register_date">
                                        <p>
                                            На сайте с {{ add.user_register_date }}
                                        </p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="wrap_user_phone col-12">
                                <div class="card">
                                    <div class="user_phone">
                                        <h4>{{ add.user_phone }}</h4>
                                    </div>
                                </div>
                            </div>
                        </div>
                         <div class="row">
                            <div class="wrap_price col-12 mb-2">
                                <div class="card">
                                    <div class="price">
                                        <h4>{{ add.price }} TMT</h4>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="wrap_ad_card_data col-12">
                                <div class="card">
                                    <div class="ad_card_data d-flex justify-content-center">
                                        <ul>
                                            <li>
                                                Просмотры {{ add.views }}
                                            </li>
                                            <li>
                                                {{ add.region_title }}
                                            </li>
                                            <li>
                                                {{ add_ad_date }}
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import moment from 'moment';
import { Get_Add } from '../../api/add'
export default {
    name: 'BaseProductDetail',
    data(){
        return {
            main_img: '',
            add: {},
            main_img_land: true,
            main_img_portrait:false,
            user_avatar:''
        }
    },
    computed: {
        region: function(){
            return this.$route.params.region
        },
        category: function(){
            return this.$route.params.category
        },
        slug: function(){
            return this.$route.params.slug
        },
        add_ad_date(){
            moment.locale('ru');
			return moment(this.add.add_date).fromNow();
        }
    },
    methods: {
        click_img(event){
            this.main_img = event.target.src.slice(21, event.target.src.length)
        },
        get_add(){
            Get_Add.add_detail(this.region, this.category, this.slug).then(response => {
                this.add = response
                this.main_img = this.add.images[0].image
            })
        },
        change_main_img(height,width){

            if (height > width){
                this.main_img_portrait = true
                this.main_img_land = false
            } else {
                this.main_img_land = true
                this.main_img_portrait = false
            }
        },
        load_main_img(event){
            let width = event.target.clientWidth
            let height = event.target.clientHeight
            this.change_main_img(height, width)
        }
    },
    beforeMount(){
        this.get_add()
    }
}
</script>

<style>
.chosen {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: flex-end;
    padding: 0px;
    overflow: hidden;
}
p {
    display: block;
}
.wrap_main_img {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 600px;
    overflow: hidden;
    border-bottom: 1px solid rgba(73,73, 73, 0.3);
    padding: 5px 0px;
}
.carousel {
    width: 100%;
}
.title {
    display: flex;
    justify-content: flex-start;
    margin: 8px 0px;
}
.choice_img {
    display: flex;
    justify-content: flex-start;
    align-items: flex-start;
    max-height: 80px;
    flex-wrap: wrap;
    overflow: hidden;
}
.wrap_choice_img{
    border-bottom: 1px solid rgba(73,73, 73, 0.3);
    border-top: 1px solid rgba(73,73, 73, 0.3);
    padding: 5px 0px;
}
.choice_img img {
    width: 100%;
}
.wrap_images {
    max-width: 100px;
    margin-left: 8px;
}
.img_land {
    width: 100%;
    height: auto;
}
.img_portait {
    height: 100%;
    width: auto;
}
.avatar {
    width: 100%;
    display: flex;
    justify-content: center;
}
.avatar img {
    max-width: 70px;
    height: auto;
    margin-bottom: 5px;
}
.card {
    padding: 7px;
}
.user_phone {
    display: flex;
    justify-content: center;
    align-items: center;
}
.wrap_user_phone {
    margin: 10px 0px;
}
.wrap_description {
    margin-top: 20px;
}
.description {
    font-size: 19px;
}
h4 {
    margin: 0px;
    padding: 0px;
}
</style>