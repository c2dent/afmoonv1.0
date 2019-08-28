<template>
  <div id="app" class="container p-0">
    <div class="row">
      <Header class="col-12"/>
    </div>
    <ModalLogin :loginOpened="loginOpened" @close="close_login_modal()"></ModalLogin>
  </div>
</template>

<script>
// eslint-disable-next-line
/* eslint-disable */
import HelloWorld from './components/HelloWorld.vue'
import Header from './components/Header.vue'
import ModalLogin from './components/modals/ModalLogin.vue'

export default {
  name: 'app',
  components: {
    HelloWorld,
    Header,
    ModalLogin
  },
  data () {
    return {
      loginOpened: false,
    }
  },
  methods: {
    show_login_modal (){
      this.loginOpened = true;
    },
    close_login_modal (){
      this.loginOpened = false;
    }
  },
  created() {
    this.$root.$on('show_login_modal', this.show_login_modal)
  }
}
</script>
<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
