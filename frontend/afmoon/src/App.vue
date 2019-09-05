<template>
  <div id="app" class="container p-0">
    <div class="row">
      <Header class="col-12"/>
    </div>
    <ModalLogin :loginOpened="loginOpened" @close="close_login_modal()"></ModalLogin>
    <div>
      <ModalPhoneVerification :verificationOpened="verificationOpened" @close="close_verification_modal()"></ModalPhoneVerification>
    </div>
  </div>
</template>

<script>
// eslint-disable-next-line
/* eslint-disable */
import HelloWorld from './components/HelloWorld.vue'
import Header from './components/Header.vue'
import ModalLogin from './components/modals/ModalLogin.vue'
import ModalPhoneVerification from './components/modals/ModalPhoneVerification.vue'
import { HTTP } from './api/common'
import store from './store/index'

export default {
  name: 'app',
  components: {
    HelloWorld,
    Header,
    ModalLogin,
    ModalPhoneVerification
  },
  data () {
    return {
      loginOpened: false,
      verificationOpened: false,
    }
  },
  methods: {
    show_login_modal (){
      this.loginOpened = true;
    },
    close_login_modal (){
      this.loginOpened = false;
    },



    show_verification_modal (){
      this.verificationOpened = true;
    },
    close_verification_modal (){
      this.verificationOpened = false;
    },

    send_sms(phone_number) {
      store.dispatch('get_sms', phone_number).then(() => {
        let auth_status = store.getters.auth_status
        if (auth_status == 'begin') {
          this.close_login_modal();
          this.show_verification_modal();
        }
      })
    },
    confirm_phone (otp) {
      phone_number = store.getters.phone_number
      store.dispatch(confirm_phone, { phone_number, otp})
    },
    logout () {
      this.$store.dispatch('logout')
    }
  },
  created() {
    this.$root.$on('show_login_modal', this.show_login_modal),
    this.$root.$on('show_verification_modal', this.show_verification_modal)
    this.$root.$on('send_sms', this.send_sms)
    this.$root.$on('confirm_phone', this.confirm_phone)
    this.$root.$on('logout', this.logout)
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
