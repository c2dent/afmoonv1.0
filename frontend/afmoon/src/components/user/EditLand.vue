<template>
    <EditBaseProduct :default_data="default_data" @ChangeData="get_data">
        <NumberInput :hint="land_area_hint"
                        @selected_number="get_land_area"
                        :default_value="default_data.land_area"
                        v-if="default_data"
                        >
        </NumberInput>
    </EditBaseProduct>
</template>

<script>
import NumberInput from '../custom_elements/NumberInput'
import EditBaseProduct from './EditBaseProduct'
export default {
    name: 'EditLand',
    components: {
        EditBaseProduct,
        NumberInput
    },
    props: {
        default_data: {},
    },
    data(){
        return {
            land_area_hint: "Площадь участка",
        }
    },
    methods: {
        get_land_area(number) {
            if (this.data.has('land_area')) {
                this.data.set('land_area', number)
                this.$emit('ChangeData', this.data)
            } else {
                this.data.append('land_area', number)
                this.$emit('ChangeData', this.data)
            }
        },
        get_data(data){
            this.data = data
            this.$emit('ChangeData', this.data)
        }
    }
}
</script>

<style>

</style>