<template>
    <div>
        <BaseProductDetail v-if="BaseProductDetail"></BaseProductDetail>
        <ApartmentDetail v-if="ApartmentDetail"></ApartmentDetail>
        <AvtomobilDetail v-if="AvtomobilDetail"></AvtomobilDetail>
        <HouseDetail v-if="HouseDetail"></HouseDetail>
        <LandDetail v-if="LandDetail"></LandDetail>
        <PersonalsClothesDetail v-if="PersonalsClothesDetail"></PersonalsClothesDetail>
        <PersonalsShoesDetail v-if="PersonalsShoesDetail"></PersonalsShoesDetail>
        <ResumeDetail v-if="ResumeDetail"></ResumeDetail>
        <SecondDetail v-if="SecondDetail"></SecondDetail>
        <VacancyDetail v-if="VacancyDetail"></VacancyDetail>
    </div>
</template>

<script>
import BaseProductDetail from './product_detail/BaseProductDetail.vue'
import ApartmentDetail from './product_detail/ApartmentDetail.vue'
import AvtomobilDetail from './product_detail/AvtomobilDetail.vue'
import HouseDetail from './product_detail/HouseDetail.vue'
import LandDetail from './product_detail/LandDetail.vue'
import PersonalsClothesDetail from './product_detail/PersonalsClothesDetail.vue'
import PersonalsShoesDetail from './product_detail/PersonalsShoesDetail.vue'
import ResumeDetail from './product_detail/ResumeDetail.vue'
import SecondDetail from './product_detail/SecondDetail.vue'
import VacancyDetail from './product_detail/VacancyDetail.vue'

export default {
    name: 'ProductDetail',
    components: {
        BaseProductDetail,
        ApartmentDetail,
        AvtomobilDetail,
        HouseDetail,
        LandDetail,
        PersonalsClothesDetail,
        PersonalsShoesDetail,
        ResumeDetail,
        SecondDetail,
        VacancyDetail
    },
    data(){
        return {
            BaseProductDetail: false,
            ApartmentDetail: false,
            AvtomobilDetail: false,
            HouseDetail: false,
            LandDetail: false,
            PersonalsClothesDetail: false,
            PersonalsShoesDetail: false,
            ResumeDetail: false,
            SecondDetail: false,
            VacancyDetail: false
        }
    },
    beforeMount(){
        let category = this.$route.params.category
        if (category == 'avtomobili') {
            this.AvtomobilDetail = true
        } else if (category == 'kvartiry') {
            this.ApartmentDetail = true
        } else if (category == 'doma-dachi-kottedzhi') {
            this.HouseDetail = true
        } else if (category == 'vakansii') {
            this.VacancyDetail = true
        } else if (category == 'zemelnye-uchastki') {
            this.LandDetail = true
        } else if (category == 'reziume') {
            this.ResumeDetail = true
        } else if (category == 'koliaski' || category == 'igrushki-i-igry' || category == 'podguzniki-i-gorshki' || category == 'tovary-dlia-ucheby') {
            this.SecondDetail = true
        } else {
            this.BaseProductDetail = true
        }
    }
}
</script>

<style>

</style>