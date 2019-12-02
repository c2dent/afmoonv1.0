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
    </EditBaseProduct>
</template>

<script>
import { User } from '../../api/user'
import Choices from '../custom_elements/Choices'
import EditBaseProduct from './EditBaseProduct'
export default {
    name: 'EditVacancy',
    components: {
        EditBaseProduct,
        Choices
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