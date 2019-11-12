<template>
    <div class="d-flex flex-column">
        <div class="d-flex heading">
            <h4>Параметры</h4>
        </div>
        <Choices :hint="marks" :choices="MARK" :index_array="0" @last_choices="last_mark"></Choices>
        <Choices :hint="models" :choices="MODEL" :index_array="1" v-if="MODEL" @last_choices="get_model"></Choices>
        <BooleanSelect :hint="is_new_hint" :values="is_new" @selected_radio="selected_is_new"></BooleanSelect>
        <NumberInput :hint="year_issue_hint" @change_number_input="get_year_issue"></NumberInput>
        <Choices :hint="gear_shift_hint" :choices="GEAR_SHIFT" :index_array="1" @last_choices="get_gear_shift_choice"></Choices>
        <Choices :hint="body_type_hint" :choices="BODY_TYPE" :index_array="1" @last_choices="get_body_type_choice"></Choices>
        <Choices :hint="engine_type_hint" :choices="ENGINE_TYPE" :index_array="1" @last_choices="get_engine_type_choice"></Choices>
        <Choices :hint="drive_unit_hint" :choices="DRIVE_UNIT" :index_array="1" @last_choices="get_drive_unit_choice"></Choices>
        <NumberInput :hint="moleage_hint" @change_number_input="get_mileage"></NumberInput>
        <BooleanSelect :hint="condition_hint" :values="condition" @selected_radio="selected_condition"></BooleanSelect>
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
    computed: {
        data () {
            return new FormData();
        }
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
        get_model(model) {
            if (this.data.has('mark_model')) {
                this.data.set('mark_model', model[0])
                this.$emit('ChangeData', this.data)
            } else {
                this.data.append('mark_model', model[0])
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
            this.data.delete('images[]')
            this.add_image(images)
            this.$emit('ChangeData', this.data)
        },
        add_image(images){
            for(let i=0; i<images.length; i++){
                this.data.append('images[]', images[i], images[i].name)
            }
        },
        selected_is_new(type_buy){
            if (this.data.has('is_new')) {
                this.data.set('is_new', type_buy)
                this.$emit('ChangeData', this.data)
            } else {
                this.data.append('is_new', type_buy)
                this.$emit('ChangeData', this.data)
            }
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
                this.data.set('gear_shift', choice[0])
                this.$emit('ChangeData', this.data)
            } else {
                this.data.append('gear_shift', choice[0])
                this.$emit('ChangeData', this.data)
            }
        },
        get_body_type_choice(choice){
            if (this.data.has('body_type')) {
                this.data.set('body_type', choice[0])
                this.$emit('ChangeData', this.data)
            } else {
                this.data.append('body_type', choice[0])
                this.$emit('ChangeData', this.data)
            }
        },
        get_engine_type_choice(choice){
            if (this.data.has('engine_type')) {
                this.data.set('engine_type', choice[0])
                this.$emit('ChangeData', this.data)
            } else {
                this.data.append('engine_type', choice[0])
                this.$emit('ChangeData', this.data)
            }
        },
        get_drive_unit_choice(choice){
            if (this.data.has('drive_unit')) {
                this.data.set('drive_unit', choice[0])
                this.$emit('ChangeData', this.data)
            } else {
                this.data.append('drive_unit', choice[0])
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
                this.data.set('condition', type_buy)
                this.$emit('ChangeData', this.data)
            } else {
                this.data.append('condition', type_buy)
                this.$emit('ChangeData', this.data)
            }
        },
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