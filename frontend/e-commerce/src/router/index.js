import { createRouter, createWebHistory } from 'vue-router';

const routes = [
  { path: '/', component: () => import('../views/home.vue') },
  { path: '/product/:id', component: () => import('../views/product.vue') },
  { path: '/sign-in', component: () => import('../views/login.vue') },
  { path: '/sign-up', component: () => import('../views/cadastro.vue') },
  { path: '/search/:name', component: () => import('../views/SearchProduct.vue') },
  { path: '/checkout', component: () => import('../views/checkout.vue') },
  { path: '/controlpanel', component: () => import('../views/controlpanel.vue') },
  { path: '/controlpanel/pedidos', component: () => import('../views/pedidos.vue') },
  { path: '/controlpanel/cartoes', component: () => import('../views/cartoes.vue') },
  { path: '/controlpanel/atividade', component: () => import('../views/atividade.vue') }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
