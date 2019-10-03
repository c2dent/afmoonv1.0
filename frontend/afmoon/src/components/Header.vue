<template>
	<div id="wrap">
		<nav>
			<div class="container">
				<div class="row">
					<div class="col-12 col-sm-12 col-md-3">
						<div class="container">
							<div class="row">
								<div class="col-4 col-sm-4 col-md-6 order-2 order-sm-2 order-md-1 d-flex align-self-center justify-content-center justify-content-md-start">
									<a class="navbar-brand" href="#">Logo</a>
								</div>
								<div class="d-none d-sm-none d-md-block col-md-6 order-md-2">
									<button class="btn btn-outline-success h35" data-toggle="modal" data-target="#Filter">
										Филтьр
									</button>
								</div>
								<div class="col-4 col-sm-4 d-md-none order-1 d-flex justify-content-start align-self-center p-0">
									<button>
										<font-awesome-icon icon="sliders-h" size="lg"></font-awesome-icon>
									</button>
								</div>
								<div class="col-4 col-sm-4 d-md-none d-flex justify-content-end align-items-center order-3 p-0">
									<div v-if="authorization">
										<router-link to="/profile"><img :src="'http://127.0.0.1:8000' + profile.avatar"  class="rounded-circle"></router-link>
									</div>
									<div v-else>
										<button>
											<font-awesome-icon icon="user" size="lg" @click="show_login"></font-awesome-icon>
										</button>
									</div>
								</div>
							</div>
						</div>
					</div>
					<div class="col-12 col-sm-12 col-md-8 p-0">
						<div class="container">
							<form action="#" class="form-inline">
								<div class="col-10 p-0">
									<input type="text" placeholder="Search" class="form-control mr-sm-2 w-100 input-group-sm h35">
								</div>
								<div class="col-2 d-flex justify-content-end p-0">
									<button class="btn btn-outline-success d-none d-sm-block pl-1 h35" type="submit">Serach</button>
									<button class="d-sm-none">
										<font-awesome-icon icon="search" size="lg"></font-awesome-icon>
									</button>
								</div>
							</form>
						</div>
					</div>
					<div class="col-md-1 d-none d-sm-none d-md-block" v-if="authorization">
						<router-link to="/profile/ads"><img :src="'http://127.0.0.1:8000' + profile.avatar"  class="rounded-circle"></router-link>
					</div>
					<div class="col-md-1 d-none d-sm-none d-md-block" v-else>
						<button class="btn btn-outline-success h35" @click="show_login">Войти</button>
					</div>
				</div>
			</div>
		</nav>
	</div>
</template>
<script>
import store from '../store/index'
export default{
	name: 'Header',
	components: {
	},
	computed: {
		profile (){
			return store.getters.get_profile
		}
	},
	data (){
		return {
			authorization: false
		}
	},
	methods: {
		show_login () {
			this.$root.$emit('show_login_modal');
		},
		logout () {
			this.$root.$emit('logout')
		}
	},
	beforeMount () {
		const token = localStorage.getItem('user-token')
		if (token) {
			this.authorization = true
			store.dispatch('get_profile')
		}
	}
}
</script>
<style scoped>
.h35 {
	height:31px;
	padding:0px 7px;
}
img {
	max-width:34px !important;
	max-height: auto !important;
}
</style>
