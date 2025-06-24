import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/home.vue';
import Product from '../views/product.vue';
import SearchProduct from '../views/SearchProduct.vue';
import Login from '../views/login.vue';
import Cadastro from '../views/cadastro.vue';
import checkout from '../views/checkout.vue'
import controlpanel  from '../views/controlpanel.vue'
import pedidos from '../views/pedidos.vue';
import cartoes from '../views/cartoes.vue';
import atividade from '../views/atividade.vue';
const routes = [
  { path: '/', component: Home },
  { path: '/product/:id', component: Product },
  // { path: '/', component: SearchProduct } 
  {path: '/sign-in', component: Login},
  { path: '/sign-up', component: Cadastro },
  { path: '/search/:name', component: SearchProduct },
  { path: '/checkout', component: checkout},
  { path: '/controlpanel', component: controlpanel},
  { path: '/controlpanel/pedidos', component: pedidos},
  { path: '/controlpanel/cartoes', component: cartoes},
  { path: '/controlpanel/atividade', component: atividade}

];

const router = createRouter({
  history: createWebHistory(), // Use createWebHistory() para evitar erros de roteamento
  routes
});

export default router; // 🔥 Não esqueça de exportar o router corretamente
