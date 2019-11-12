 <template>
    <div class="d-flex flex-column">
        <div class="d-flex heading">
            <h4>Параметры</h4>
        </div>
        <Choices :hint="size_hint" :choices="SIZE_SHOES" :index_array="1" @last_choices="get_size"></Choices>
        <TitleInput @ChangeInput="get_title"></TitleInput>
        <DescriptionText @ChangeDescription="get_description"></DescriptionText>
        <PriceInput @ChangePrice="get_price"></PriceInput>
        <InputImage @ChangeImages="get_images"></InputImage>
    </div>
</template>

<script>
import { User } from '../../api/user'
import TitleInput from '../custom_elements/TitleInput'
import PriceInput from '../custom_elements/PriceInput'
import InputImage from '../custom_elements/InputImage'
import DescriptionText from '../custom_elements/DescriptionText'
import Choices from '../custom_elements/Choices'
export default {
    name: 'PersonalsClothes',
    components: {
        TitleInput,
        DescriptionText,
        PriceInput,
        InputImage,
        Choices,
    },
    computed: {
        data () {
            return new FormData();
        }
    },
    data(){
        return {
            size_hint:"Размер",
            SIZE_SHOES: null,
        }
    },
    methods: {
        get_size_shoes(){
            User.get_choices("SIZE_SHOES").then(response => {
                this.SIZE_SHOES = response
            })
        },
        get_title(title){
            if (this.data.has('title')) {
                this.data.set('title', title)
                this.$emit('ChangeData', this.data)
            } else {
                this.data.append('title', title)
                this.$emit('ChangeData', this.data)
            }
        },
        get_description(description){
            if (this.data.has('description')) {
                this.data.set('description', description)
                this.$emit('ChangeData', this.data)
            } else {
                this.data.append('description', description)
                this.$emit('ChangeData', this.data)
            }
        },
        get_price(price){
            if (this.data.has('price')) {
                this.data.set('price', price)
                this.$emit('ChangeData', this.data)
            } else {
                this.data.append('price', price)
                this.$emit('ChangeData', this.data)
            }
        },
        get_images(images){
            this.data.delete('images[]')
            this.add_image(images)
            this.$emit('ChangeData', this.data)
        },
        add_image(images){
            for(let i=0; i<images.length; i++){
                this.data.append('images[]', images[i], images[i].name)
            }
        },
        get_size(choice){
            if (this.data.has('size')) {
                this.data.set('size', choice[0])
                this.$emit('ChangeData', this.data)
            } else {
                this.data.append('size', choice[0])
                this.$emit('ChangeData', this.data)
            }
        },
    },
    beforeMount(){
        this.get_size_shoes()
    }
}
</script>

<style>
.heading {
    margin: 25px 0px;
    font-weight: 600;
}
</style>