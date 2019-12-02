<template>
    <EditBaseProduct :default_data="default_data" @ChangeData="get_data">
        <Choices :hint="size_hint"
                    :choices="SIZE_SHOES"
                    :index_array="1"
                    :back_value="0"
                    @last_choices="get_size"
                    :default_value="default_data.size">
    </Choices>
    </EditBaseProduct>
</template>

<script>
import { User } from '../../api/user'
import Choices from '../custom_elements/Choices'
import EditBaseProduct from './EditBaseProduct'
export default {
    name: 'EditPersonalsShoes',
    components: {
        EditBaseProduct,
        Choices
    },
    props: {
        default_data: {},
    },
    data(){
        return {
            size_hint:"Размер",
            SIZE_SHOES: null,
        }
    },
    methods: {
        get_size_shoes(){
            User.get_choices("SIZE_SHOES").then(response => {
                this.SIZE_SHOES = response
            })
        },
        get_size(choice){
            if (this.data.has('size')) {
                this.data.set('size', choice)
                this.$emit('ChangeData', this.data)
            } else {
                this.data.append('size', choice)
                this.$emit('ChangeData', this.data)
            }
        },
        get_data(data){
            this.data = data
            this.$emit('ChangeData', this.data)
        }
    },
    beforeMount(){
        this.get_size_shoes()
    }
}
</script>

<style>

</style>