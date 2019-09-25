<template>
  <div id="app" class="container p-0">
    <div class="row">
      <Header class="col-12"/>
    </div>
    <ModalLogin :loginOpened="loginOpened" @close="close_login_modal()"></ModalLogin>
    <div>
      <ModalPhoneVerification :verificationOpened="verificationOpened" @close="close_verification_modal()"></ModalPhoneVerification>
    </div>
    <div id="content">
      <router-view></router-view>
    </div>
    <div id="footer">

    </div>
  </div>
</template>

<script>
// eslint-disable-next-line
/* eslint-disable */
import Header from './components/Header.vue'
import ModalLogin from './components/modals/ModalLogin.vue'
import ModalPhoneVerification from './components/modals/ModalPhoneVerification.vue'
import Profile from './components/Profile.vue'
import store from './store/index'

export default {
  name: 'app',
  components: {
    Header,
    ModalLogin,
    ModalPhoneVerification,
    Profile
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
      store.dispatch('get_sms', { phone_number }).then(() => {
        console.log(store.getters.auth_status)
        if (store.getters.auth_status == 'begin') {
          this.close_login_modal();
          this.show_verification_modal();
        }
      })
    },
    confirm_phone(otp) {
      let phone_number = store.getters.phone_number
      let otp_key = localStorage.getItem('otp_key')
      store.dispatch('confirm_phone', { phone_number, otp, otp_key})
    },
    logout () {
        store.dispatch('logout').then(() => {
        console.log('all good')
      })
    },
    test (phone_number) {
      console.log(phone_number)
      this.close_login_modal();
      this.show_verification_modal();
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