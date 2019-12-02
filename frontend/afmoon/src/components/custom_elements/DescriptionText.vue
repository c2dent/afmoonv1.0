<template>
    <div id="wrap">
        <div class="container">
            <div class="row">
                <div class="col-2 d-flex">
                    <span>Описания</span>
                </div>
                <div class="col-8 d-flex">
                    <textarea name="" id="" cols="30" rows="8" class="form-control mr-sm-2 w-100 input-group-sm" v-model="description" @change="get_description">
                    </textarea>
                </div>
                <div class="col-2">

                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        default_value:{}
    },
    name: 'DescriptionText',
    data(){
        return {
            description:''
        }
    },
    methods: {
        get_description(){
            this.$emit('ChangeDescription', this.description)
        }
    },
    beforeMount(){
        this.description = this.default_value
        this.get_description()
    }
}
</script>

<style>
textarea {
    padding: 0%;
}
</style>