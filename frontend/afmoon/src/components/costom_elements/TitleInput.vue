<template>
    <div id="wrap">
        <div class="container">
            <div class="row">
                <div class="col-2 d-flex">
                    <span>Названия</span>
                </div>
                <div class="col-8 d-flex">
                    <input type="text" name="title" class="form-control mr-sm-2 w-100 input-group-sm h33">
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
}
</script>

<style scoped>
input {
    padding: 0px;
}
</style>