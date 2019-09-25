<template>
    <div class="settings">
        <p class="settings-headline">
            Личные настройки
        </p>
        <ul class="settings-list">
            <li class="pl-4">
                <div class="d-flex justify-content-between align-items-center">
                    <div>
                        <p class="font-weight-bold">Имя</p>
                        <p class="info"> {{ profile.nickname }}</p>
                    </div>
                    <div>
                        <button class="btn btn-link">Изменить</button>
                    </div>
                </div>
            </li>
            <li class="pl-4">
                <div class="d-flex justify-content-between align-items-center">
                    <div>
                        <p class="font-weight-bold">Номер телефона</p>
                        <p class="info"> {{ profile.phone_number }}</p>
                    </div>
                    <div>
                        <button class="btn btn-link">Изменить</button>
                    </div>
                </div>
            </li>
            <li class="pl-4">
                <div class="d-flex justify-content-between align-items-center">
                    <div>
                        <p class="font-weight-bold">Местоположения</p>
                        <p class="info"> {{ profile.region }}</p>
                    </div>
                    <div>
                        <button class="btn btn-link">Изменить</button>
                    </div>
                </div>
            </li>
        </ul>
        <p class="settings-headline">
            Общие настройки
        </p>
        <ul class="settings-list">
            <li class="pl-4">
                <div class="d-flex justify-content-between align-items-center">
                    <div>
                        <p class="font-weight-bold">Черный список</p>
                    </div>
                    <div>
                        <button class="btn btn-link">Изменить</button>
                    </div>
                </div>
            </li>
            <li class="pl-4">
                <div class="d-flex justify-content-between align-items-center">
                    <div>
                        <p class="font-weight-bold">Уведомления</p>
                    </div>
                    <div>
                        <button class="btn btn-link">Изменить</button>
                    </div>
                </div>
            </li>
        </ul>
    </div>
</template>

<script>
import store from '../store/index'
export default {
    name: 'UserSettings',
    computed: {
        profile () {
            return store.getters.get_profile
        }
    }

}
</script>

<style scope>
.settings {
    text-align: start;
}
.settings-headline {
    font-size: 25px;
    font-style: bold;
}
.settings-list li{
    border: 1px solid rgba(73,73, 73, 0.1);
    width: 100%;
    list-style-type: none;
    padding: 5px 10px;
}
ul {
    padding: 0px;
    margin: 15px 0px 20px 0px;
}
ul li:hover {
    background-color: rgb(240, 240, 240);
}
.info {
    color: #075AB4;
}
.h35 {
    max-height: 31px !important;
}
</style>