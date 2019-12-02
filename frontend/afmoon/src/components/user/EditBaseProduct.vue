<template>
    <div class="d-flex flex-column">
        <div class="d-flex heading">
            <h4>Параметры</h4>
        </div>
        <TitleInput @ChangeInput="get_title" :default_value="default_data.title" v-if="default_data"></TitleInput>
        <slot></slot>
        <DescriptionText @ChangeDescription="get_description" :default_value="default_data.description" v-if="default_data"></DescriptionText>
        <PriceInput @ChangePrice="get_price" :default_value="default_data.price" v-if="default_data"></PriceInput>
        <InputImage @ChangeImages="get_images" :default_value="images" v-if="default_data"></InputImage>
    </div>
</template>

<script>
import TitleInput from '../custom_elements/TitleInput'
import PriceInput from '../custom_elements/PriceInput'
import InputImage from '../custom_elements/InputImage'
import DescriptionText from '../custom_elements/DescriptionText'
export default {
    name: 'EditBaseProduct',
    props: {
        default_data: {},
    },
    components: {
        TitleInput,
        DescriptionText,
        PriceInput,
        InputImage,
    },
    computed: {
        data: function() {
            return new FormData();
        },
        images: function () {
            if (this.default_data.images){
                let imgs=[]
                for (let i = 0; i < this.default_data.images.length; i++) {
                    imgs.push('http://127.0.0.1:8000' + this.default_data.images[i].image)
                }
                return imgs
            } else {
                return null
            }
        }
    },
    methods: {
        get_title(title){
            if (this.data.has('title')) {
                this.data.set('title', title)
                this.$emit('ChangeData', this.data)
            } else {
                this.data.append('title', title)
                this.$emit('ChangeData', this.data)
            }
        },
        get_description(description){
            if (this.data.has('description')) {
                this.data.set('description', description)
                this.$emit('ChangeData', this.data)
            } else {
                this.data.append('description', description)
                this.$emit('ChangeData', this.data)
            }
        },
        get_price(price){
            if (this.data.has('price')) {
                this.data.set('price', price)
                this.$emit('ChangeData', this.data)
            } else {
                this.data.append('price', price)
                this.$emit('ChangeData', this.data)
            }
        },
        get_images(images){
            this.delete_image()
            this.add_image(images)
            this.$emit('ChangeData', this.data)
        },
        delete_image(){
            this.data.delete('images[]')
            this.data.delete('image')
        },
        add_image(imgs){
            if (imgs){
                this.data.append('image', imgs[0], imgs[0].name)
                for(let i=0; i<imgs.length; i++){
                    this.data.append('images[]', imgs[i], imgs[i].name)
                }
            }
        }
    },
    beforeMount(){
        if (this.default_data){
            this.get_title(this.default_data.title)
            if (this.default_data.description) {
                this.get_description(this.default_data.description)
            }
            if (this.default_data.price) {
                this.get_price(this.default_data.price)
            }
        }
    }
}
</script>

<style>
.heading {
    margin: 25px 0px;
    font-weight: 600;
}
</style>