<template>
    <div id="wrap">
        <div class="container">
            <div class="row">
                <div class="col-2 d-flex">
                    <span>
                        Фотографии
                    </span>
                </div>
                <div class="col-8 d-flex">
                    <div class="container">
                        <div class="row">
                            <div class="image-upload">
                                <label for="file-input">
                                    <img src="../../static/icon/add_phone_png"/>
                                </label>
                                <input id="file-input" type="file" accept="image/*"/>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-2">
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import image from ""
export default {
    name: 'InputImage',
    data(){
        return {
            images: [],
        }
    }
}
</script>

<style>
</style>