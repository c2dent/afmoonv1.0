<template>
    <div>
        <select @change="onChange()" v-model="select_element">
            <option value="" disabled selected hidden>Выберите</option>
            <option v-for="element in select_array" v-bind:key="element.id" :value="element">{{ element.title }}</option>
        </select>
    </div>
</template>

<script>
export default {
    name: 'FormSelect',
    data () {
        return {
            select_element: {},
        }
    },
    props: {
        select_array: null,
        default_value: {}
    },
    methods: {
        onChange() {
            this.$emit('OnSelect', this.select_element)
        }
    },
    beforeMount(){
        if (this.default_value) {
            this.select_element = this.default_value
        }
    }
}
</script>

<style>

</style>