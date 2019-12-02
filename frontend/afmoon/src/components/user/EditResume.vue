<template>
    <EditBaseProduct :default_data="default_data" @ChangeData="get_data">
        <Choices :hint="schedule_hint"
                    :choices="SCHEDULE"
                    :index_array="1"
                    @last_choices="get_schedule_choice"
                    :back_value="0"
                    :default_value="default_data.schedule"
                    v-if="default_data"
                    >
        </Choices>
        <Choices :hint="work_experience_hint"
                    :choices="WORK_EXPERIENCE"
                    :index_array="1"
                    @last_choices="get_work_experience_choice"
                    :back_value="0"
                    :default_value="default_data.work_experience"
                    v-if="default_data"
                    >
        </Choices>
        <NumberInput :hint="age_hint"
                        @selected_number="get_age"
                        :default_value="default_data.age"
                        v-if="default_data"
                        >
        </NumberInput>
        <BooleanSelect :hint="gender_hint"
                        :values="gender"
                        @selected_radio="selected_gender"
                        :default_value="default_data.gender"
                        v-if="default_data"
                        >
        </BooleanSelect>
    </EditBaseProduct>
</template>

<script>
import { User } from '../../api/user'
import Choices from '../custom_elements/Choices'
import NumberInput from '../custom_elements/NumberInput'
import BooleanSelect from '../custom_elements/BooleanSelect'
import EditBaseProduct from './EditBaseProduct'
export default {
    name: 'EditResume',
    components: {
        EditBaseProduct,
        Choices,
        NumberInput,
        BooleanSelect
    },
    props: {
        default_data: {},
    },
    data(){
        return {
            schedule_hint: 'График работы',
            SCHEDULE: null,
            work_experience_hint:'Опыть работы',
            WORK_EXPERIENCE: null,
            age_hint:"Возраст",
            gender_hint: "Пол",
            gender: [[true,"Мужской"], [false,"Женский"]],
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
        get_schedule_choice(choice){
            if (this.data.has('schedule')) {
                this.data.set('schedule', choice)
                this.$emit('ChangeData', this.data)
            } else {
                this.data.append('schedule', choice)
                this.$emit('ChangeData', this.data)
            }
        },
        get_work_experience_choice(choice){
            if (this.data.has('work_experience')) {
                this.data.set('work_experience', choice)
                this.$emit('ChangeData', this.data)
            } else {
                this.data.append('work_experience', choice)
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
                this.data.set('gender', type_buy)
                this.$emit('ChangeData', this.data)
            } else {
                this.data.append('gender', type_buy)
                this.$emit('ChangeData', this.data)
            }
        },
        get_data(data){
            this.data = data
            this.$emit('ChangeData', this.data)
        }
    },
    beforeMount() {
        this.get_schedule()
        this.get_work_experience()
    }
}
</script>

<style>

</style>