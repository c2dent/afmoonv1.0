<template>
    <div class="d-flex flex-column">
        <TitleInput></TitleInput>
        <DescriptionText></DescriptionText>
        <PriceInput></PriceInput>
        <InputImage></InputImage>
    </div>
</template>

<script>
import TitleInput from '../costom_elements/TitleInput'
import PriceInput from '../costom_elements/PriceInput'
import InputImage from '../costom_elements/InputImage'
import DescriptionText from '../costom_elements/DescriptionText'
export default {
    name: 'BaseProduct',
    components: {
        TitleInput,
        DescriptionText,
        PriceInput,
        InputImage,
    }
}
</script>

<style>
</style>