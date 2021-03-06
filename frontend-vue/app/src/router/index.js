import Vue from 'vue'
import Router from 'vue-router'

import Index from '@/components/Index'
import Login from '@/components/Login'
import ListBooks from '@/components/Books/List'
import EditBook from'@/components/Books/Edit'
import ListCharacters from '@/components/Characters/List'
import EditCharacter from'@/components/Characters/Edit'

Vue.use(Router)

export default new Router({
  mode: 'history',
  hash: false,
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/books',
      name: 'ListBooks',
      component: ListBooks
    },
    {
      path: '/books/edit/:id',
      name: 'EditBook',
      component: EditBook
    },
    {
      path: '/characters',
      name: 'ListCharacters',
      component: ListCharacters
    },
    {
      path: 'characters/edit/:id',
      name: 'EditCharacters',
      component: EditCharacter
    }
  ]
})
