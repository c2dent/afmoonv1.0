<template>
    <div id="wrap">
        <div class="container">
            <div class="row">
                <div class="d-flex col-2">
                    <span>Цена</span>
                </div>
                <div class="d-flex col-8">
                    <input type="number" name="title" class="form-control mr-sm-2 input-group-sm h33" @change="send_price" v-model="price">
                </div>
                <div class="col-2">

                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'PriceInput',
    props: {
        default_value: {},
    },
    data(){
        return {
            price:'',
        }
    },
    methods: {
        send_price(){
            this.$emit('ChangePrice', this.price)
        }
    },
    beforeMount(){
        this.price = this.default_value
        this.send_price()
    }
}
</script>

<style>
input {
    padding: 0px;
}
</style>