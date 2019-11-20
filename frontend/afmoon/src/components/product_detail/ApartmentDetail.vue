<template>
    <div>
        <BaseProductDetail v-slot:default="ad_props">
            <div class="container p-0 m-0">
                <div class="row wrap_additional_data">
                    <div class="col-6 d-flex m-0 p-0">
                        <p>Этажы в доме:&nbsp;&nbsp;</p><b>{{ ad_props.add.floors_in_house }}</b>
                    </div>
                    <div class="col-6 m-0 p-0 d-flex">
                        <p>Количество комнат:&nbsp;&nbsp;</p><b>{{ ad_props.add.number_rooms }}</b>
                    </div>
                    <div class="col-6 m-0 p-0 d-flex">
                        <p>Этаж:&nbsp;&nbsp;</p><b>{{ ad_props.add.floor }}</b>
                    </div>
                    <div class="col-6 m-0 p-0 d-flex">
                        <p>Общая площадь:&nbsp;&nbsp;</p><b>{{ ad_props.add.total_area }}&nbsp;&nbsp;м <sup>2</sup></b>
                    </div>
                    <div class="col-6 p-0 m-0 d-flex">
                        <p>Тип продажи:&nbsp;&nbsp;</p><b>{{ ad_props.add.rent_buy }}</b>
                    </div>
                </div>
            </div>
        </BaseProductDetail>
    </div>
</template>

<script>
import BaseProductDetail from './BaseProductDetail'
export default {
    name: 'ApartmentDetail',
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