<template>
    <div id="wrap">
        <div class="container">
            <div class="row">
                <div class="d-flex col-2">
                    <span>{{ hint }}</span>
                </div>
                <div class="d-flex col-8">
                    <div v-for="val in values" class="wrap_input" v-bind:key="val">
                        <input type="radio" v-bind:value="val" v-model="radio_boolean" :id="'group' + val" @change="OnChange">
                        <label :for="'group' + val">{{ val }}</label>
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
    },
    data() {
        return {
            radio_boolean: false,
        }
    },
    methods: {
        OnChange(){
            this.$emit('selected_redio', this.radio_boolean)
        }
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