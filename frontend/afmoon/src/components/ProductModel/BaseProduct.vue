<template>
    <div class="d-flex flex-column">
        <div class="d-flex heading">
            <h4>Параметры</h4>
        </div>
        <TitleInput @ChangeInput="get_title"></TitleInput>
        <DescriptionText @ChangeDescription="get_description"></DescriptionText>
        <PriceInput @ChangePrice="get_price"></PriceInput>
        <InputImage @ChangeImages="get_images"></InputImage>
    </div>
</template>

<script>
import TitleInput from '../custom_elements/TitleInput'
import PriceInput from '../custom_elements/PriceInput'
import InputImage from '../custom_elements/InputImage'
import DescriptionText from '../custom_elements/DescriptionText'
export default {
    name: 'BaseProduct',
    components: {
        TitleInput,
        DescriptionText,
        PriceInput,
        InputImage,
    },
    computed: {
        data () {
            return new FormData();
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
        },
        add_image(images){
            for(let i=0; i<images.length; i++){
                this.data.append('images[]', images[i], images[i].name)
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