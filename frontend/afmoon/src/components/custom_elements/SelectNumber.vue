<template>
    <div id="wrap">
        <div class="container">
            <div class="row">
                <div class="d-flex col-2">
                    <span>{{ hint }}</span>
                </div>
                <div class="d-flex col-8">
                    <select>
                        <option v-for="number in numbers" v-bind:value="number">{{ number }}</option>
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
    name: 'NumberInput',
    props: {
        hint: '',
        numbers: 0,
    }
}
</script>

<style>
input {
    padding: 0px;
}
</style>