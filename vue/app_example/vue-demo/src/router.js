import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'

Vue.use(Router);

export default new Router({
    routes: [
        {
            path: "/",
            name: "home",
            component: Home
        },
        {
            path: "/1.4",
            name: "触发组件更新",
            component: () => import("./views/1.4")
        },
        {
            path: "/1.5",
            name: "计算属性和侦听器",
            component: () => import("./views/1.5")
        },
    ]
});