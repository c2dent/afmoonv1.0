<template>
    <div>
        <div>
            {{ user }}
        </div>
    </div>
</template>

<script>
import { User } from '../api/user'
export default {
    name: 'UserDetail',
    data() {
        return {
            user: ''
        }
    },
    computed: {
        get_id: function(){
            return this.$route.params.id
        }
    },
    methods: {
        get_user(){
            User.user_detail(this.get_id).then(response => {
                this.user = response
            })
        }
    },
    beforeMount(){
        this.get_user()
    }
}
</script>

<style scoped>

</style>