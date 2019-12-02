<template>
    <EditBaseProduct :default_data="default_data" @ChangeData="get_data">
        <SelectNumber :hint="hint_floors"
                        :numbers="floor"
                        @selected_number="get_hint_floors"
                        :default_value="default_data.floors_in_house"
                        v-if="default_data"></SelectNumber>
        <SelectNumber :hint="hint_floor"
                        :numbers="floor"
                        @selected_number="get_hint_floor"
                        :default_value="default_data.floor"
                        v-if="default_data"></SelectNumber>
        <NumberInput :hint="hint_area"
                        @change_number_input="get_total_area"
                        :default_value="default_data.total_area"
                        v-if="default_data"></NumberInput>
        <Choices :hint="number_in_room"
                    :choices="NUMBER_ROOMS"
                    :index_array="1"
                    @last_choices="get_number_room"
                    :default_value="default_data.number_rooms"
                    :back_value="0"
                    v-if="default_data"></Choices>
        <BooleanSelect :hint="type_buy"
                        :values="values"
                        @selected_radio="selected_type_bay"
                        :default_value="default_data.rent_buy"></BooleanSelect>
    </EditBaseProduct>
</template>

<script>
import { User } from '../../api/user'
import EditBaseProduct from './EditBaseProduct'
import SelectNumber from '../custom_elements/SelectNumber'
import NumberInput from '../custom_elements/NumberInput'
import BooleanSelect from '../custom_elements/BooleanSelect'
import Choices from '../custom_elements/Choices'
export default {
    name: 'EditApartment',
    components: {
        EditBaseProduct,
        SelectNumber,
        NumberInput,
        BooleanSelect,
        Choices
    },
    props: {
        default_data: {},
    },
    data(){
        return {
            hint_floors: "Этажы в доме",
            hint_floor: "Этаж",
            floor: 25,
            hint_area : "Общая площадь",
            type_buy: 'Тир продажи',
            values : [[true,'Продам'], [false, 'Сдам']],
            number_in_room: "Комнаты в квартире",
            NUMBER_ROOMS: null,
            data: {},
        }
    },
    methods: {
        get_number_rooms(){
            User.get_choices("NUMBER_ROOMS").then(response => {
                this.NUMBER_ROOMS = response
            })
        },
        get_number_room(choice){
            if (this.data.has('number_rooms')) {
                this.data.set('number_rooms', choice[0])
                this.$emit('ChangeData', this.data)
            } else {
                this.data.append('number_rooms', choice[0])
                this.$emit('ChangeData', this.data)
            }
        },
        selected_type_bay(type_buy){
            if (this.data.has('rent_buy')) {
                if (type_buy  == 'Продам'){
                    this.data.set('rent_buy', true)
                } else {
                    this.data.set('rent_buy', false)
                }
                this.$emit('ChangeData', this.data)
            } else {
                if (type_buy == 'Продам'){
                    this.data.append('rent_buy', true)
                } else {
                    this.data.append('rent_buy', false)
                }
                this.$emit('ChangeData', this.data)
            }
        },
        get_total_area(number) {
            if (this.data.has('total_area')) {
                this.data.set('total_area', number)
                this.$emit('ChangeData', this.data)
            } else {
                this.data.append('total_area', number)
                this.$emit('ChangeData', this.data)
            }
        },
        get_hint_floor(number) {
            if (this.data.has('floor')) {
                this.data.set('floor', number)
                this.$emit('ChangeData', this.data)
            } else {
                this.data.append('floor', number)
                this.$emit('ChangeData', this.data)
            }
        },
        get_hint_floors(number) {
            if (this.data.has('floors_in_house')) {
                this.data.set('floors_in_house', number)
                this.$emit('ChangeData', this.data)
            } else {
                this.data.append('floors_in_house', number)
                this.$emit('ChangeData', this.data)
            }
        },
        get_data(data){
            this.data = data
            this.$emit('ChangeData', this.data)
        }
    },
    beforeMount(){
        this.get_number_rooms()
    }
}
</script>

<style>

</style>