<template>
    <div id="wrap">
        <div>
            <div class="d-flex heading">
                <h4>Выберите категории</h4>
            </div>
            <div class="wrap_categor">
                <div v-for="element_array in element_arrays" v-bind:value="element_array">
                    <FormSelect :select_array="element_array" @OnSelect="OnSelect" class="form_select"></FormSelect>
                </div>
            </div>
        <div>

        </div>
        </div>
    </div>
</template>

<script>
import { User } from '../../api/user'
import FormSelect from '../custom_elements/FormSelect'
export default {
    name: "ChoiceCategory",
    components: {
        FormSelect,
    },
    data() {
        return {
            element_arrays: [],
        }
    },
    methods: {
        get_categories(level=null, lft=null, rght=null){
            User.category(level,lft,rght).then(response => {
                this.element_arrays.push(response)
            })
        },
        OnSelect(element){
            const level = element.level
            if (element.rght - element.lft > 1){
                this.$emit('OnChange')
                this.element_arrays.splice(level, this.element_arrays.length - level)
                this.get_categories(element.level +1, element.lft, element.rght)
            } else {
                this.$emit('OnSelect')
            }
        }
    },
    beforeMount(){
        this.get_categories("1")
    }
}
</script>

<style>
.wrap_categor {
    display: flex;
    flex-wrap: wrap;
}
</style>