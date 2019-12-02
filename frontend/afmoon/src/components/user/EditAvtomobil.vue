<template>
    <EditBaseProduct :default_data="default_data" @ChangeData="get_data">
        <Choices :hint="marks"
                    :choices="MARK"
                    :index_array="0"
                    :back_value="1"
                    @last_choices="last_mark"
                    :default_value="default_data.mark"
                    v-if="default_data"
                    >
        </Choices>
        <Choices :hint="models"
                    :choices="MODEL"
                    :index_array="1"
                    :back_value="0"
                    @last_choices="get_model"
                    :default_value="default_data.model"
                    v-if="default_data"
                    >
        </Choices>
        <NumberInput :hint="year_issue_hint"
                        @change_number_input="get_year_issue"
                        :default_value="default_data.year_issue"
                        v-if="default_data"
                        >
        </NumberInput>
        <Choices :hint="gear_shift_hint"
                    :choices="GEAR_SHIFT"
                    :index_array="1"
                    @last_choices="get_gear_shift_choice"
                    :back_value="0"
                    :default_value="default_data.gear_shift"
                    v-if="default_data"
                    >
        </Choices>
        <Choices :hint="body_type_hint"
                    :choices="BODY_TYPE"
                    :index_array="1"
                    @last_choices="get_body_type_choice"
                    :back_value="0"
                    :default_value="default_data.body_type"
                    v-if="default_data"
                    >
        </Choices>
        <Choices :hint="engine_type_hint"
                    :choices="ENGINE_TYPE"
                    :index_array="1"
                    @last_choices="get_engine_type_choice"
                    :back_value="0"
                    :default_value="default_data.engine_type"
                    v-if="default_data"
                    >
        </Choices>
        <Choices :hint="drive_unit_hint"
                    :choices="DRIVE_UNIT"
                    :index_array="1"
                    @last_choices="get_drive_unit_choice"
                    :back_value="0"
                    :default_value="default_data.drive_unit"
                    v-if="default_data"
                    >
        </Choices>
        <NumberInput :hint="moleage_hint"
                        @change_number_input="get_mileage"
                        :default_value="default_data.mileage"
                        v-if="default_data"
                        >
        </NumberInput>
        <BooleanSelect :hint="condition_hint"
                        :values="condition"
                        @selected_radio="selected_condition"
                        :default_value="default_data.condition"
                        v-if="default_data"
                        >
        </BooleanSelect>
    </EditBaseProduct>
</template>

<script>
import EditBaseProduct from './EditBaseProduct'
import { User } from '../../api/user'
import BooleanSelect from '../custom_elements/BooleanSelect'
import NumberInput from '../custom_elements/NumberInput'
import Choices from '../custom_elements/Choices'
export default {
    name: 'EditAvtomobil',
    components: {
        EditBaseProduct,
        Choices,
        BooleanSelect,
        NumberInput
    },
    props: {
        default_data: {},
    },
    data(){
        return {
            MARK: null,
            marks: "Марка",
            MODEL: null,
            models: "Модели",
            year_issue_hint: 'Год выпуска',
            GEAR_SHIFT: null,
            gear_shift_hint: 'Коробка передач',
            BODY_TYPE: null,
            body_type_hint: 'Тип кузова',
            ENGINE_TYPE: null,
            engine_type_hint: 'Тип двигателя',
            moleage_hint:'Пробег',
            DRIVE_UNIT: null,
            drive_unit_hint: 'Привод',
            condition: [[false,"Битый"], [true, "Не битый"]],
            condition_hint: "Состояние"
        }
    },
    methods: {
        get_mark (){
            User.get_choices("MARK").then(response => {
                this.MARK = response
            })
        },
        last_mark(mark){
            this.MODEL = mark
            this.get_gear_shift()
            this.get_body_type()
            this.get_engine_type()
            this.get_drive_unit()
        },
        get_model(model) {
            if (this.data.has('mark_model')) {
                this.data.set('mark_model', model)
                this.$emit('ChangeData', this.data)
            } else {
                this.data.append('mark_model', model)
                this.$emit('ChangeData', this.data)
            }
        },
        get_gear_shift (){
            User.get_choices("GEAR_SHIFT").then(response => {
                this.GEAR_SHIFT = response
            })
        },
        get_body_type(){
            User.get_choices("BODY_TYPE").then(response => {
                this.BODY_TYPE = response
            })
        },
        get_engine_type(){
            User.get_choices('ENGINE_TYPE').then(response => {
                this.ENGINE_TYPE = response
            })
        },
        get_drive_unit(){
            User.get_choices('DRIVE_UNIT').then(response => {
                this.DRIVE_UNIT = response
            })
        },
        get_year_issue(number) {
            if (this.data.has('year_issue')) {
                this.data.set('year_issue', number)
                this.$emit('ChangeData', this.data)
            } else {
                this.data.append('year_issue', number)
                this.$emit('ChangeData', this.data)
            }
        },
        get_gear_shift_choice(choice){
            if (this.data.has('gear_shift')) {
                this.data.set('gear_shift', choice)
                this.$emit('ChangeData', this.data)
            } else {
                this.data.append('gear_shift', choice)
                this.$emit('ChangeData', this.data)
            }
        },
        get_body_type_choice(choice){
            if (this.data.has('body_type')) {
                this.data.set('body_type', choice)
                this.$emit('ChangeData', this.data)
            } else {
                this.data.append('body_type', choice)
                this.$emit('ChangeData', this.data)
            }
        },
        get_engine_type_choice(choice){
            if (this.data.has('engine_type')) {
                this.data.set('engine_type', choice)
                this.$emit('ChangeData', this.data)
            } else {
                this.data.append('engine_type', choice)
                this.$emit('ChangeData', this.data)
            }
        },
        get_drive_unit_choice(choice){
            if (this.data.has('drive_unit')) {
                this.data.set('drive_unit', choice)
                this.$emit('ChangeData', this.data)
            } else {
                this.data.append('drive_unit', choice)
                this.$emit('ChangeData', this.data)
            }
        },
        get_mileage(number) {
            if (this.data.has('mileage')) {
                this.data.set('mileage', number)
                this.$emit('ChangeData', this.data)
            } else {
                this.data.append('mileage', number)
                this.$emit('ChangeData', this.data)
            }
        },
        selected_condition(type_buy){
            if (this.data.has('condition')) {
                if (type_buy == 'Не битый'){
                    this.data.set('condition', true)
                } else {
                    this.data.set('condition', true)
                }
                this.$emit('ChangeData', this.data)
            } else {
                if (type_buy == 'Не битый'){
                    this.data.append('condition', false)
                } else {
                    this.data.append('condition', false)
                }
                this.$emit('ChangeData', this.data)
            }
        },
        get_data(data){
            this.data = data
            this.$emit('ChangeData', this.data)
        }
    },
    beforeMount(){
        this.get_mark()
    }
}
</script>

<style>

</style>