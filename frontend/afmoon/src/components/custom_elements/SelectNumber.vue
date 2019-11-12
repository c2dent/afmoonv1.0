<template>
    <div id="wrap">
        <div class="container">
            <div class="row">
                <div class="d-flex col-2">
                    <span>{{ hint }}</span>
                </div>
                <div class="d-flex col-8">
                    <select @change="OnChange()" v-model="select_number">
                        <option v-for="number in numbers" v-bind:key="number" :value="number">{{ number }}</option>
                    </select>
                </div>
                <div class="col-2">

                </div>
            </div>
        </div>
    </div>
</template>

<script>
// eslint-disable-next-line
/* eslint-disable */
export default {
    name: 'NumberInput',
    props: {
        hint: '',
        numbers: 0,
    },
    data(){
        return {
            select_number: ''
        }
    },
    methods: {
        OnChange(){
            this.$emit('selected_number', this.select_number)
        }
    }
}
</script>

<style>
input {
    padding: 0px;
}
</style>