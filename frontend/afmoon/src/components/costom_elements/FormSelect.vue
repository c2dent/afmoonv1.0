<template>
    <div>
        <form action="#">
            <select @change="onChange($event)" v-model="cat">
                <option selected>Выберите</option>
                <option v-for="cat in categories" v-bind:value="cat">{{ cat.title }}</option>
            </select>
        </form>
    </div>
</template>

<script>
export default {
    name: 'FormSelect',
    data () {
        return {
            cat: {},
        }
    },
    props: ['categories'],
    methods: {
        onChange() {
            this.$emit('cat_up', this.cat)
        }
    }
}
</script>

<style>

</style>