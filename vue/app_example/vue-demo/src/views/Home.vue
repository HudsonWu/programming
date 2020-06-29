<template>
    <div id="nav">
        <template v-for="{ key, name } in list">
            <div :key="key" style="padding: 10px 0">
                <router-link :to="`/${key}`">{{ name }}章节</router-link>
            </div>
        </template>
    </div>
</template>

<script>
export default {
    name: 'Home',
    data() {
        return {
            list: [
                {
                    key: "1.4",
                    name: "如何触发组件的更新"
                },
                {
                    key: "1.5",
                    name: "合理应用计算属性和侦听器"
                }
            ]
        };
    }
};
</script>

<style lang="less">
#nav {
  padding: 30px;
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>