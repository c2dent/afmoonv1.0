<template>
    <div class="d-flex flex-column">
        <div class="d-flex heading">
            <h4>Параметры</h4>
        </div>
        <TitleInput></TitleInput>
        <Choices :hint="marks" :choices="MARK" :index_array="0" @last_choices="last_mark"></Choices>
        <Choices :hint="models" :choices="MODEL" :index_array="1" v-if="MODEL"></Choices>
        <BooleanSelect :hint="is_new_hint" :values="is_new"></BooleanSelect>
        <NumberInput :hint="year_issue_hint"></NumberInput>
        <Choices :hint="gear_shift_hint" :choices="GEAR_SHIFT" :index_array="1"></Choices>
        <Choices :hint="body_type_hint" :choices="BODY_TYPE" :index_array="1"></Choices>
        <Choices :hint="engine_type_hint" :choices="ENGINE_TYPE" :index_array="1"></Choices>
        <Choices :hint="drive_unit_hint" :choices="DRIVE_UNIT" :index_array="1"></Choices>
        <NumberInput :hint="moleage_hint"></NumberInput>
        <BooleanSelect :hint="condition_hint" :values="condition"></BooleanSelect>
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
import Choices from '../custom_elements/Choices'
import DescriptionText from '../custom_elements/DescriptionText'
import BooleanSelect from '../custom_elements/BooleanSelect'
import NumberInput from '../custom_elements/NumberInput'
export default {
    name: 'Avtomobil',
    components: {
        TitleInput,
        DescriptionText,
        PriceInput,
        InputImage,
        Choices,
        BooleanSelect,
        NumberInput,
    },
    data(){
        return {
            MARK: null,
            marks: "Марка",
            MODEL: null,
            models: "Модели",
            is_new:['Новый','С пробегам'],
            is_new_hint: 'Тип автомобиля',
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
            condition: ["Битый", "Не битый"],
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
            this.MODEL = mark[1]
            this.get_gear_shift()
            this.get_body_type()
            this.get_engine_type()
            this.get_drive_unit()
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
        }
    },
    beforeMount(){
        this.get_mark()
    }
}
</script>

<style>
.heading {
    margin: 25px 0px;
    font-weight: 600;
}
</style>