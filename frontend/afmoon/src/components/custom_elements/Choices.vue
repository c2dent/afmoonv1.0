<template>
    <div id="wrap">
        <div class="container">
            <div class="row">
                <div class="d-flex col-2">
                    <span>{{ hint }}</span>
                </div>
                <div class="d-flex col-8">
                    <select @change="onChange" v-model="choice">
                        <option value="" disabled selected style='display:none;'>Выберите</option>
                        <option v-for="val in choices" v-bind:key="val[index_array]" :value="val[back_value]">{{ val[index_array] }}</option>
                    </select>
                </div>
                <div class="col-2">

                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Choices',
    props: {
        hint: null,
        choices: null,
        index_array: null,
        default_value:{},
        back_value: null,
    },
    data(){
        return {
            choice: null,
        }
    },
    methods: {
        onChange(){
            this.$emit('last_choices', this.choice)
        },
    },
    beforeMount(){
        if (this.default_value){
            this.choice = this.default_value
        }
        this.onChange()
    }
}
</script>

<style>
input {
    padding: 0px;
}
option {
    min-width: 150px;
}
</style>