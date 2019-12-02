<template>
    <div id="wrap">
        <div class="container">
            <div class="row">
                <div class="col-2 d-flex">
                    <span>Названия</span>
                </div>
                <div class="col-8 d-flex">
                    <input type="text" name="title" class="form-control mr-sm-2 w-100 input-group-sm h33" v-model="title_input" @change="OnChange" required>
                </div>
                <div class="col-2">
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'TitleInput',
    props: {
        default_value: {},
    },
    data(){
        return {
            title_input: '',
        }
    },
    methods: {
        OnChange(){
            this.$emit('ChangeInput', this.title_input)
        }
    },
    beforeMount(){
        this.title_input = this.default_value
        this.OnChange()
    }
}
</script>

<style scoped>
input {
    padding: 0px;
}
</style>