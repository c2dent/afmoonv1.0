<template>
    <div class="d-flex flex-column">
        <div class="d-flex heading">
            <h4>Параметры</h4>
        </div>
        <Choices :hint="schedule_hint" :choices="SCHEDULE" :index_array="1" @last_choices="get_schedule_choice"></Choices>
        <Choices :hint="work_experience_hint" :choices="WORK_EXPERIENCE" :index_array="1" @last_choices="get_work_experience_choice"></Choices>
        <TitleInput @ChangeInput="get_title"></TitleInput>
        <DescriptionText @ChangeDescription="get_description"></DescriptionText>
        <PriceInput @ChangePrice="get_price"></PriceInput>
        <InputImage @ChangeImages="get_images"></InputImage>
    </div>
</template>

<script>
import { User } from '../../api/user'
import TitleInput from '../custom_elements/TitleInput'
import PriceInput from '../custom_elements/PriceInput'
import InputImage from '../custom_elements/InputImage'
import Choices from '../custom_elements/Choices'
import DescriptionText from '../custom_elements/DescriptionText'
export default {
    name: 'Vacancy',
    components: {
        TitleInput,
        DescriptionText,
        PriceInput,
        InputImage,
        Choices,
    },
    computed: {
        data () {
            return new FormData();
        }
    },
    data(){
        return {
            schedule_hint: 'График работы',
            SCHEDULE: null,
            work_experience_hint:'Опыть работы',
            WORK_EXPERIENCE: null,
        }
    },
    methods: {
        get_schedule(){
            User.get_choices("SCHEDULE").then(response => {
                this.SCHEDULE = response
            })
        },
        get_work_experience(){
            User.get_choices("WORK_EXPERIENCE").then(response => {
                this.WORK_EXPERIENCE = response
            })
        },
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
        add_image(images){
            this.data.append('image', images[0], images[0].name)
            for(let i=0; i<images.length; i++){
                this.data.append('images[]', images[i], images[i].name)
            }
        },
        get_schedule_choice(choice){
            if (this.data.has('schedule')) {
                this.data.set('schedule', choice[0])
                this.$emit('ChangeData', this.data)
            } else {
                this.data.append('schedule', choice[0])
                this.$emit('ChangeData', this.data)
            }
        },
        get_work_experience_choice(choice){
            if (this.data.has('work_experience')) {
                this.data.set('work_experience', choice[0])
                this.$emit('ChangeData', this.data)
            } else {
                this.data.append('work_experience', choice[0])
                this.$emit('ChangeData', this.data)
            }
        }
    },
    beforeMount() {
        this.get_schedule()
        this.get_work_experience()
    }
}
</script>

<style>
.heading {
    margin: 25px 0px;
    font-weight: 600;
}
</style>