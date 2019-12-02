<template>
    <div id="wrap">
        <div class="container">
            <div class="row">
                <div class="d-flex col-2">
                    <span>{{ hint }}</span>
                </div>
                <div class="d-flex col-8">
                    <div v-for="val in values" class="wrap_input" v-bind:key="val[0]">
                        <input type="radio" v-bind:value="val[0]" v-model="radio_boolean" :id="'group' + val" @change="OnChange">
                        <label :for="'group' + val">{{ val[1] }}</label>
                    </div>
                </div>
                <div class="col-2">

                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'BooleanSelect',
    props: {
        hint : null,
        values: {},
        default_value:{},
    },
    data() {
        return {
            radio_boolean: false,
        }
    },
    methods: {
        OnChange(){
            this.$emit('selected_radio', this.radio_boolean)
        }
    },
    beforeMount(){
        this.radio_boolean = this.default_value
    }
}
</script>

<style>
.wrap_input {
    margin-right: 20px;
    margin-left: 0px;
}
.wrap_input>input {
    margin-right:5px;
    display: inline-block;
}
.wrap_input>label {
    display: inline-block;
}
</style>