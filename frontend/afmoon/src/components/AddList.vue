<template>
  <div class="wrap">
      <div class="container">
          <div class="row">
              <div class="col-2">

              </div>
              <div class="col-8">
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
            region : 'turkmenistan',
            add_list: {},
        }
    },
    methods: {
        by_region (){
            Get_Add.by_region(this.region).then(response => {
                this.add_list = response
            })
        }
    },
    beforeMount (){
        this.by_region()
    }
}
</script>

<style>

</style>