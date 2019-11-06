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
export default {
    name: 'NumberInput',
    props: {
        hint: '',
    },
    data(){
        return {
            number : 0
        }
    },
    methods: {
        OnChange(){
            this.$emit('change_number_input', this.number)
        }
    }

}
</script>

<style>
input {
    padding: 0px;
}
</style>