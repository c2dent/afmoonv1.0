<template>
    <div>
        <ModalBase :ModalOpened="ModalFilter" @close="close_modal">
            <div id="wrap">
                <div class="container">
                    <div class="row">
                        <div class="col-12">
                            <h3>
                                Выберите регион
                            </h3>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-12 d-flex">
                            <FormSelect :select_array="REGIONS" @OnSelect="OnSelectRegion" :default_value="region"></FormSelect>
                        </div>
                    </div>
                </div>
                <div class="container mt-3 mb-3">
                    <div class="row">
                        <div class="col-12">
                            <h3>
                                Выберите категрии
                            </h3>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-12 d-flex">
                            <FormSelect :select_array="CATEGORIES" @OnSelect="OnSelectCategory"></FormSelect>
                        </div>
                    </div>
                </div>
                <div>
                    <button class="btn btn-outline-success h35 mb-1" @click="reload_url" :disabled="isButtonDisabled">Применить</button>
                </div>
            </div>
        </ModalBase>
    </div>
</template>

<script>
import FormSelect from '../custom_elements/FormSelect'
import { User } from '../../api/user'
import ModalBase from './ModalBase'
import store from '../../store/index'
export default {
    name: 'ModalFilter',
    components: {
        ModalBase,
        FormSelect,
    },
    props: {
        ModalFilter: {}
    },
    data(){
        return {
            REGIONS: {},
            CATEGORIES: {},
            isButtonDisabled: true,
        }
    },
    computed: {
        region (){
            return store.getters.region
        },
        category (){
            return store.getters.category
        }
    },
    methods: {
        close_modal(){
            this.$emit('close')
        },
        OnSelectRegion(elm){
            store.dispatch('set_region', elm)
            this.ChangeFilter()
        },
        OnSelectCategory(elm){
            store.dispatch('set_category', elm)
            this.ChangeFilter()
        },
        get_regions(){
            User.region().then(response => {
                this.REGIONS = response
            })
        },
        get_categories(){
            User.category().then(response => {
                this.CATEGORIES = response
            })
        },
        reload_url(){
            if (this.category){
                if(this.region){
                    this.$router.push('/' + this.region.slug + '/' + this.category.slug + '/')
                } else {
                    this.$router.push('/turkmenistan/' + this.category.slug + '/')
                }
            } else if (this.region){
                this.$router.push('/' + this.region.slug + '/')
            }
            location.reload()
            this.$emit('close')
        },
        ChangeFilter(){
            if (this.region() || this.category){
                this.isButtonDisabled = false
            }
        }
    },
    beforeMount(){
        this.get_regions()
        this.get_categories()

    }
}
</script>

<style scoped>

</style>