<template>
    <div class="d-flex flex-column">
        <div class="d-flex heading">
            <h4>Параметры</h4>
        </div>
        <TitleInput></TitleInput>
        <SelectNumber :hint="hint_floors" :numbers="floor"></SelectNumber>
        <SelectNumber :hint="hint_floor" :numbers="floor"></SelectNumber>
        <NumberInput :hint="hint_area"></NumberInput>
        <NumberInput :hint="hint_area"></NumberInput>
        <Choices :hint="number_in_room" :choices="NUMBER_ROOMS" :index_array="1"></Choices>
        <BooleanSelect :hint="type_buy" :values="vaules"></BooleanSelect>
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
    methods: {
        get_number_rooms(){
            User.get_choices("NUMBER_ROOMS").then(response => {
                this.NUMBER_ROOMS = response
            })
        }
    },
    beforeMount () {
    }
}
</script>

<style>
.heading {
    margin: 25px 0px;
    font-weight: 600;
}
</style>