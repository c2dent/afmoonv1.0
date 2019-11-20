<template>
    <div class="d-flex flex-column">
        <div class="d-flex heading">
            <h4>Параметры</h4>
        </div>
        <Choices :hint="schedule_hint" :choices="SCHEDULE" :index_array="1" @last_choices="get_schedule_choice"></Choices>
        <Choices :hint="work_experience_hint" :choices="WORK_EXPERIENCE" :index_array="1" @last_choices="get_work_experience_choice"></Choices>
        <NumberInput :hint="age_hint" @change_number_input="get_age"></NumberInput>
        <BooleanSelect :hint="gender_hint" :values="gender" @selected_radio="selected_gender"></BooleanSelect>
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
import NumberInput from '../custom_elements/NumberInput'
import Choices from '../custom_elements/Choices'
import DescriptionText from '../custom_elements/DescriptionText'
import BooleanSelect from '../custom_elements/BooleanSelect'
export default {
    name: 'Resume',
    components: {
        TitleInput,
        DescriptionText,
        PriceInput,
        InputImage,
        NumberInput,
        Choices,
        BooleanSelect,
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
            age_hint:"Возраст",
            gender_hint: "Пол",
            gender: ["Мужской", "Женский"],
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
        },
        get_age(number) {
            if (this.data.has('age')) {
                this.data.set('age', number)
                this.$emit('ChangeData', this.data)
            } else {
                this.data.append('age', number)
                this.$emit('ChangeData', this.data)
            }
        },
        selected_gender(type_buy){
            if (this.data.has('gender')) {
                if (type_buy == 'Мужской') {
                    this.data.set('gender', true)
                } else {
                    this.data.set('gender', false)
                }
                this.$emit('ChangeData', this.data)
            } else {
                if (type_buy == 'Мужской') {
                    this.data.append('gender', true)
                } else {
                    this.data.append('gender', false)
                }
                this.$emit('ChangeData', this.data)
            }
        },
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