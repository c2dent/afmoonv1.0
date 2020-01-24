<template>
	<transition name="modal">
		<div class="modal_wrap" v-if="verificationOpened">
			<div class="modal_background" @click="close_verification_modal"></div>
			<div class="container shadow bg-white pl-sm-5 pr-sm-5 pb-sm-5 pl-3 pr-3 pb-3" id="modal">
				<div id="close_modal">
					<button @click="close_verification_modal">
						<font-awesome-icon icon="times" size="lg"></font-awesome-icon>
					</button>
				</div>
				<div class="col-12 mb-3 pb-0 pb-sm-1">
					<a href="#">
						<h2>AFMOON</h2>
					</a>
				</div>
				<div class="col-12">
					<form @submit.prevent="confirm_phone">
						<span class="hint">Мы отправили на вашу номер SMS с кодом пожалуюста введите код пароля для потверждении телефона</span>
						<fieldset class="form-group">
							<input type="tel" id="phone" class="form-control" required placeholder="SMS код" v-model="otp">
							<button class="again" type="button">отправить еще раз</button>
						</fieldset>
						<div>
							<button class="btn btn-outline-success h35 m-2" type="submit">
								Потвердить
							</button>
						</div>
					</form>
				</div>
			</div>
		</div>
	</transition>
</template>
<script>
// eslint-disable-next-line
/* eslint-disable */
export default {
	name: 'ModalPhoneVerification',
	props: {
		verificationOpened : {
			type : Boolean,
		},
	},
	data () {
		return {
			otp: ""
		}
	},
	methods: {
		close_verification_modal () {
			this.$emit('close')
		},
		confirm_phone (){
			this.$root.$emit('confirm_phone', this.otp)
		}
	},
}
</script>
<style scoped>
.modal_wrap, .modal_background{
	position: fixed;
	left: 0px;
	top: 0px;
	width: 100%;
	height: 100%;
}
.modal_background {
	z-index: 40;
	background-color:green;
	background-color: rgba(210, 210, 210, 0.3)

}
.modal_wrap{
	display: flex;
	justify-content: center;
	align-items: center;
	transition:all 1s;
	z-index: 10;
}
.modal_content{
	display: flex;
	flex-direction: column;
	border-radius: 5px;
	padding: 60px 60px;
	z-index: 50;
	background-color: black;
}
#modal {
	z-index:100;
	border-radius: 7px;
	max-width:400px;
	transition: all 1s;
	position:relative;
}
.again {
	display: inline-block;
	font-size:10px;
	background-color:white;
	border:none;
}
.again:hover {
	color:green;
}
.hint {
	display:block;
	padding-bottom: 20px;
}
input{
	border:none;
	border-radius:0px;
	box-shadow:none;
	padding:0px;
	background-color: #DBDBDB
}
input:focus {
	border:none;
	border-radius:0px;
	box-shadow:none;
	background-color: #DBDBDB
}
fieldset {
	display:flex;
	flex-direction:row;
	align-items:center;
	margin-top:20px;
	margin-bottom:20px;
}
.modal-enter,
.modal-leave-active {
	opacity: 0;
}
.modal-enter #modal,
.modal-leave-active #modal {
	-webkit-transform: scale(1.1);
	transform: scale(1.1);
}
#close_modal{
	position:absolute;
	top: 5px;
	right: 5px;
}
</style>