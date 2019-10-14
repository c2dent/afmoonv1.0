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
                            <div class="col-2 image-wrap" v-for="imge in images" v-bind:key="imge">
                                <AddImage :image="imge" @delete_img="DeleteImg"></AddImage>
                            </div>
                            <div class="col-2">
                                <div class="image-upload">
                                    <label for="file-input">
                                        <img src="../../static/icon/add_photo.png" class="add-img"/>
                                    </label>
                                    <input id="file-input" type="file" accept="image/*" @change="fileChange($event)"/>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
// eslint-disable-next-line
/* eslint-disable */
import AddImage from './AddImage'
export default {
    name: 'InputImage',
    components: {
        AddImage,
    },
    data(){
        return {
            images: [],
        }
    },
    methods: {
        fileChange(evt) {
            const file = evt.target.files[0];
            this.images.push(URL.createObjectURL(file));
        },
        DeleteImg(imge){
            var index = this.images.indexOf(imge);
            if (index > -1) {
                this.images.splice(index, 1);
            }
        }
    }
}
</script>

<style scoped>
.image-upload>input {
    display: none;
}
.add-img:hover {
    cursor: pointer;
}
.add-img {
    max-width: 100%;
    height:100%;
    padding: 0px;
    margin: 0px;
}
.image-upload {
    width: 100%;
    height: 100%;
    padding: 0px;
    margin: 0px;
    overflow: hidden;
}
.image-upload:hover {
    cursor: pointer;
    background-color: #efe8e8;
}
.image-wrap {
    padding: 0px;
    height: 100px;
    width: 100px;
}
.image-upload>label {
    padding: 0px;
    margin: 0px;
}
</style>