<template>
    <div>
        <BaseProductDetail v-slot:default="ad_props">
            <div class="container p-0 m-0">
                <div class="row wrap_additional_data">
                    <div class="col-6 d-flex m-0 p-0">
                        <p>Марка:&nbsp;&nbsp;</p><b>{{ ad_props.add.mark }}</b>
                    </div>
                    <div class="col-6 p-0 m-0 d-flex">
                        <p>Коробка передач:&nbsp;&nbsp;</p><b>{{ ad_props.add.gear_shift }}</b>
                    </div>
                    <div class="col-6 m-0 p-0 d-flex">
                        <p>Модель:&nbsp;&nbsp;</p><b>{{ ad_props.add.model }}</b>
                    </div>
                    <div class="col-6 m-0 p-0 d-flex">
                        <p>Год выпуска:&nbsp;&nbsp;</p><b>{{ ad_props.add.year_issue }}</b>
                    </div>
                    <div class="col-6 p-0 m-0 d-flex">
                        <p>Тип кузова:&nbsp;&nbsp;</p><b>{{ ad_props.add.body_type }}</b>
                    </div>
                    <div class="col-6 p-0 m-0 d-flex">
                        <p>Тип двигателя:&nbsp;&nbsp;</p><b>{{ ad_props.add.engine_type }}</b>
                    </div>
                    <div class="col-6 p-0 m-0 d-flex">
                        <p>Пробег:&nbsp;&nbsp;</p><b>{{ ad_props.add.mileage }}</b>
                    </div>
                    <div class="col-6 p-0 m-0 d-flex">
                        <p>Привод:&nbsp;&nbsp;</p><b>{{ ad_props.add.drive_unit }}</b>
                    </div>
                    <div class="col-6 p-0 m-0 d-flex">
                        <p>Состояние:&nbsp;&nbsp;</p><b>{{ ad_props.add.condition }}</b>
                    </div>
                </div>
            </div>
        </BaseProductDetail>
    </div>
</template>

<script>
import BaseProductDetail from './BaseProductDetail'
export default {
    name: 'AvtomobilDetail',
    components: {
        BaseProductDetail
    }
}
</script>

<style>
.wrap_additional_data {
    margin: 25px 0px;
    padding: 10px 7px 0px 10px;
    background-color: #f2f2f2;
    border-radius: 7px;
}
</style>