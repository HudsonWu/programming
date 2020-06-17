<template>
  <div id="app">
    {{message}} {{message + " " + message}}
    <!-- <div v-bind:id="message"></div> -->
    <!-- 使用v-bind指令可以渲染动态值，v-bind:，可以简写为: -->
    <div :id="message"></div>
    <todo-list>
      <todo-item @delete="handleDelete" v-for="item in list" :key="item.title" :title="item.title" :del="item.del">
        <template v-slot:pre-icon="{value}">
          <slot>前置图标 {{value}}</slot>
        </template>
        <template v-slot:suf-icon>
          <slot>后置图标</slot>
        </template>
      </todo-item>
    </todo-list>
  </div>
</template>

<script>
import TodoList from './components/TodoList.vue'
import TodoItem from './components/TodoItem.vue'

export default {
  name: 'App',
  components: {
    TodoList,
    TodoItem
  },
  data() {
    return {
      message: 'hello world',
      list: [{
        title: '课程1',
        del: false
      }, {
        title: '课程2',
        del: true
      }],
    }
  },
  methods: {
    handleDelete(val) {
      console.log('handleDelete', val)
    }
  }
}
</script>
