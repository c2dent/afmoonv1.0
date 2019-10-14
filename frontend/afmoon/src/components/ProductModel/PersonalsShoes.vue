 <template>
    <div class="d-flex flex-column">
        <div class="d-flex heading">
            <h4>Параметры</h4>
        </div>
        <TitleInput></TitleInput>
        <Choices :hint="size_hint" :choices="SIZE_SHOES" :index_array="1"></Choices>
        <DescriptionText></DescriptionText>
        <PriceInput></PriceInput>
        <InputImage></InputImage>
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
        }
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