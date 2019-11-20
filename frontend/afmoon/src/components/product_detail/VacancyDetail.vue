<template>
    <div>
        <BaseProductDetail v-slot:default="ad_props">
            <div class="container p-0 m-0">
                <div class="row wrap_additional_data">
                    <div class="col-6 d-flex m-0 p-0">
                        <p>График работы:&nbsp;&nbsp;</p><b>{{ ad_props.add.schedule }}</b>
                    </div>
                    <div class="col-6 m-0 p-0 d-flex">
                        <p>Опыть работы:&nbsp;&nbsp;</p><b>{{ ad_props.add.work_experience }}</b>
                    </div>
                </div>
            </div>
        </BaseProductDetail>
    </div>
</template>

<script>
import BaseProductDetail from './BaseProductDetail'
export default {
    name: 'VacancyDetail',
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