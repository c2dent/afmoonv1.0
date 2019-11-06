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
    props: ['select_array'],
    methods: {
        onChange() {
            this.$emit('OnSelect', this.select_element)
        }
    }
}
</script>

<style>

</style>