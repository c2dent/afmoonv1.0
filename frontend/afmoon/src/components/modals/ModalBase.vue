<template>
	<transition name="modal">
		<div class="modal_wrap" v-if="ModalOpened">
			<div class="modal_background" @click="closeModal"></div>
			<div class="container shadow bg-white pl-sm-5 pr-sm-5 pb-sm-2 pl-3 pr-3 pb-1" id="modal">
				<div id="close_modal">
					<button @click="closeModal" class="close_modal">
						<font-awesome-icon icon="times" size="lg"></font-awesome-icon>
					</button>
				</div>
				<div class="row">
					<div class="col-12 mb-3 pb-0 pb-sm-1">
						<a href="#">
							<h2>AFMOON</h2>
						</a>
					</div>
				</div>
				<div class="row">
					<slot></slot>
				</div>
			</div>
		</div>
	</transition>
</template>
<script>
// eslint-disable-next-line
/* eslint-disable */
export default {
	name: 'ModalBase',
	props: {
		ModalOpened : false
	},
	data () {
		return {
			phone_number : ""
		}
	},
	methods: {
		closeModal() {
			this.$emit('close')
		},
		show_verification (){
			this.$root.$emit('show_modal_base')
		}
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
	z-index: 10;
}
.modal_content{
	display: flex;
	flex-direction: column;
	border-radius: 3px;
	padding: 60px 60px;
	z-index: 50;
	background-color: black;
}
#modal {
	border-radius: 3px;
	max-width:460px;
	transition: all 1s;
	position:relative;
	z-index:1000;
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
.h35 {
	height:31px;
	padding:0px 7px;
}
#close_modal{
	position:absolute;
	top: 0px;
	right: 0px;
	padding: 0px;
	margin: 0px;
}
.close_modal{
	padding: 0px;
	border: none;
}
.close_modal:active {
	border: none;
}
</style>