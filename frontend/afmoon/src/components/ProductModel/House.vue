<template>
    <div class="d-flex flex-column">
        <div class="d-flex heading">
            <h4>Параметры</h4>
        </div>
        <TitleInput></TitleInput>
        <NumberInput :hint="house_area_hint"></NumberInput>
        <NumberInput :hint="land_area_hint"></NumberInput>
        <DescriptionText></DescriptionText>
        <PriceInput></PriceInput>
        <InputImage></InputImage>
    </div>
</template>

<script>
import TitleInput from '../custom_elements/TitleInput'
import PriceInput from '../custom_elements/PriceInput'
import InputImage from '../custom_elements/InputImage'
import NumberInput from '../custom_elements/NumberInput'
import DescriptionText from '../custom_elements/DescriptionText'
export default {
    name: 'House',
    components: {
        TitleInput,
        DescriptionText,
        PriceInput,
        InputImage,
        NumberInput,
    },
    data(){
        return {
            house_area_hint: "Площадь дома",
            land_area_hint: "Площадь участка",
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