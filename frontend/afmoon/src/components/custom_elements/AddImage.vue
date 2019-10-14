<template>
    <div class="wrap">
        <figure>
            <img :src="image">
            <img src="../../static/icon/delete.png" class="delete" @click="DeleteImg">
        </figure>
    </div>
</template>

<script>
export default {
    name:'AddImage',
    props: {
        image: null
        },
    methods: {
        DeleteImg() {
            this.$emit('delete_img', this.image)
        }
    }
}
</script>
<style scoped>
.wrap {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 100%;
    padding: 4px !important;
    overflow: hidden;
}
img {
    max-width: 100%;
    height: 100%;
    margin: 0px !important;
}
figure {
    padding: 0px;
    margin: 0px !important;
    width: 100%;
    height: 100%;
    position: relative;
}
.reload {
    position: absolute;
    top: 2px;
    left: 3px;
    max-width: 25px;
    height: auto;
}
.delete {
    position: absolute;
    top: 4px;
    right: 4px;
    max-width: 16px;
    height: auto;
    padding: 2px;
    background-color: azure;
    border-radius: 50%;
}
.delete:hover {
    cursor: pointer;
}
</style>