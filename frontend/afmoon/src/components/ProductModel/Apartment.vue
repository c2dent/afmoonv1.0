<template>
    <div class="d-flex flex-column">
        <div class="d-flex heading">
            <h4>Параметры</h4>
        </div>
        <TitleInput @ChangeInput="get_title"></TitleInput>
        <SelectNumber :hint="hint_floors" :numbers="floor" @selected_number="get_hint_floors"></SelectNumber>
        <SelectNumber :hint="hint_floor" :numbers="floor" @selected_number="get_hint_floor"></SelectNumber>
        <NumberInput :hint="hint_area" @change_number_input="get_total_area"></NumberInput>
        <Choices :hint="number_in_room" :choices="NUMBER_ROOMS" :index_array="1" @last_choices="get_number_room"></Choices>
        <BooleanSelect :hint="type_buy" :values="vaules" @selected_radio="selected_type_bay"></BooleanSelect>
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
import DescriptionText from '../custom_elements/DescriptionText'
import NumberInput from '../custom_elements/NumberInput'
import SelectNumber from '../custom_elements/SelectNumber'
import BooleanSelect from '../custom_elements/BooleanSelect'
import Choices from '../custom_elements/Choices'
export default {
    name: 'Apartment',
    components: {
        TitleInput,
        DescriptionText,
        PriceInput,
        InputImage,
        NumberInput,
        SelectNumber,
        BooleanSelect,
        Choices,
    },
    data() {
        return {
            hint_floors: "Этажы в доме",
            hint_floor: "Этаж",
            floor: 25,
            hint_area : "Общая площадь",
            type_buy: 'Тир продажи',
            vaules : ['Продам', 'Сдам'],
            number_in_room: "Комнаты в квартире",
            NUMBER_ROOMS: null,
        }
    },
    computed: {
        data () {
            return new FormData();
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
                this.data.set('rent_buy', type_buy)
                this.$emit('ChangeData', this.data)
            } else {
                this.data.append('rent_buy', type_buy)
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
        get_images(images){
            this.data.delete('images[]')
            this.add_image(images)
            this.$emit('ChangeData', this.data)
        },
        add_image(images){
            for(let i=0; i<images.length; i++){
                this.data.append('images[]', images[i], images[i].name)
            }
        },

    },
    beforeMount () {
        this.get_number_rooms()
    }
}
</script>

<style>
.heading {
    margin: 25px 0px;
    font-weight: 600;
}
</style>