<template>
	<transition name="modal">
		<div class="modal_wrap" v-if="loginOpened">
			<div class="modal_background" @click="closeModalLogin"></div>
			<div class="container shadow bg-white pl-sm-5 pr-sm-5 pb-sm-5 pl-3 pr-3 pb-3" id="modal">
				<div class="col-12 mb-3 pb-0 pb-sm-1">
					<a href="#">
						<h2>AFMOON</h2>
					</a>

				</div>
				<div class="col-12 mb-4 pb-1 pb-sm-4">
					<span><i>Афмун это сайт бесплатных доска объявлении</i></span>
				</div>
				<div class="col-12">
					<form>
						<span>Пожалуюста введите свой номер телефона</span>
						<fieldset class="form-group">
							<span id="plus">+</span><input type="tel" id="phone" class="form-control" required>
						</fieldset>
						<div>
							<button class="btn btn-outline-success h35 m-2">
								Получить код для входа
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
	name: 'ModalLogin',
	props: {
		loginOpened : {
			type : Boolean,
		},
	},
	methods: {
		closeModalLogin () {
			this.$emit('close')
		},
	}
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
}
#plus {
	display:inline-block;
	height:100%;
	margin-right:6px;
	font-size:x-large;
}
input{
	border-left:none;
	border-right:none;
	border-top:none;
	border-bottom:1px solid black;
	border-radius:0px;
	box-shadow:none;
	padding:0px;
}
input:focus {
	border-left:none;
	border-right:none;
	border-top:none;
	border-bottom:1px solid black;
	border-radius:0px;
	box-shadow:none;
}
fieldset {
	display:flex;
	flex-direction:row;
	align-items:center;
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
</style>