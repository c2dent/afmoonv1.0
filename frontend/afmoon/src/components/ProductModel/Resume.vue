<template>
    <div class="d-flex flex-column">
        <div class="d-flex heading">
            <h4>Параметры</h4>
        </div>
        <TitleInput></TitleInput>
        <Choices :hint="schedule_hint" :choices="SCHEDULE" :index_array="1"></Choices>
        <Choices :hint="work_experience_hint" :choices="WORK_EXPERIENCE" :index_array="1"></Choices>
        <NumberInput :hint="age_hint"></NumberInput>
        <BooleanSelect :hint="gender_hint" :values="gender"></BooleanSelect>
        <DescriptionText></DescriptionText>
        <PriceInput></PriceInput>
        <InputImage></InputImage>
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