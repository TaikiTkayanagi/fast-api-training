import Memos from '@/views/Memos.vue'
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      redirect: '/memos',
    },
    {
      path: '/memos',
      name: 'memos',
      component: () => Memos,
    },
    {
      path: '/memos/form',
      name: 'memoForm',
      component: () => import('@/views/MemoForm.vue'),
    },
    {
      path: '/memos/:id',
      name: 'memo-detail',
      props: true,
      component: () => import('@/views/Memo.vue'),
    },
  ],
})

export default router
