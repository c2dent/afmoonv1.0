<template>
    <div class="d-flex flex-column">
        <div class="d-flex heading">
            <h4>Параметры</h4>
        </div>
        <TitleInput></TitleInput>
        <BooleanSelect :hint="second_hint" :values="second"></BooleanSelect>
        <DescriptionText></DescriptionText>
        <PriceInput></PriceInput>
        <InputImage></InputImage>
    </div>
</template>

<script>
import TitleInput from '../custom_elements/TitleInput'
import PriceInput from '../custom_elements/PriceInput'
import InputImage from '../custom_elements/InputImage'
import BooleanSelect from '../custom_elements/BooleanSelect'
import DescriptionText from '../custom_elements/DescriptionText'
export default {
    name: 'Second',
    components: {
        TitleInput,
        DescriptionText,
        PriceInput,
        InputImage,
        BooleanSelect,
    },
    data(){
        return {
            second_hint:"Состояние",
            second : ["Новый", "Б/У"],
        }
    }
}
</script>

<style>
.heading {
    margin: 25px 0px;
    font-weight: 600;
}
</style>