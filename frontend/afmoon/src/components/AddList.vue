<template>
  <div class="wrap">
      <div class="container">
          <div class="row">
              <div class="col-3">

              </div>
              <div class="col-7">
                  <Add v-for="add in add_list" v-bind:key="add.name" :add="add"></Add>
              </div>
              <div class="col-2">

              </div>
          </div>
      </div>
  </div>
</template>

<script>
import { Get_Add } from '../api/add'
import Add from './Add.vue'
export default {
    name: 'AddList',
    components: {
        Add,
    },
    data (){
        return {
            add_list: {},
        }
    },
    computed: {
        region: function(){
            return this.$route.params.region
        },
        category: function(){
            return this.$route.params.category
        }
    },
    methods: {
        by_region (){
            Get_Add.by_region(this.region).then(response => {
                this.add_list = response
            })
        },
        by_region_category(){
            Get_Add.by_region_category(this.region,this.category).then(response => {
                this.add_list = response
            })
        }
    },
    beforeMount (){
        if (this.category) {
            this.by_region_category()
        } else {
            this.by_region()
        }
    }
}
</script>

<style>

</style>