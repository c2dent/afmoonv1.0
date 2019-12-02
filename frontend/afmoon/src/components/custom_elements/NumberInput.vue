<template>
    <div id="wrap">
        <div class="container">
            <div class="row">
                <div class="d-flex col-2">
                    <span>{{ hint }}</span>
                </div>
                <div class="d-flex col-8">
                    <input type="number" name="title" class="form-control mr-sm-2 input-group-sm h33" v-model="number" @change="OnChange">
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
        default_value:{},
    },
    data(){
        return {
            number : 0
        }
    },
    methods: {
        OnChange(){
            this.$emit('selected_number', this.number)
        }
    },
    beforeMount(){
        if(this.default_value){
            this.number = this.default_value
        }
    }

}
</script>

<style>
input {
    padding: 0px;
}
</style>