<template>
    <section class="py-5"  v-for="(product, i) in products" :key="i">
  <div class="container">
    <div class="row gx-5">
      <aside class="col-lg-6">
        <div class="card prod-card border rounded-4 mb-3 d-flex justify-content-center" style="  box-shadow: 0 4px 12px rgba(0,0,0,0.1);   border-radius: 12px; height: 300px;">
          <a data-fslightbox="mygalley" class="rounded-4 object-scale-down" style="height: 300px;" target="_blank" data-type="image" :href=product.src>
            <img style="width: 100%; height: 100%; margin: auto;" class=" rounded-4 object-scale-down" :src=product.src />
          </a>
        </div>
        <div class="d-flex justify-content-center mb-3">
          <a data-fslightbox="mygalley" class=" subimg item-thumb border mx-1 rounded-2" target="_blank" data-type="image"  >
            <img width="60" height="60" class="rounded-2" :src=product.src  />
          </a>
        </div>
        <!-- thumbs-wrap.// -->
        <!-- gallery-wrap .end// -->
      </aside>
      <main class="col-lg-6">
        <div class="ps-lg-3">
          <h4 class="title text-dark">
           {{ product.name }}
          </h4>
          <!-- <div class="d-flex flex-row my-3">
            <div class="text-warning mb-1 me-2">
              <i class="fa fa-star"></i>
              <i class="fa fa-star"></i>
              <i class="fa fa-star"></i>
              <i class="fa fa-star"></i>
              <i class="fas fa-star-half-alt"></i>
              <span class="ms-1">
                4.5
              </span>
            </div>
            <span class="text-muted"><i class="fas fa-shopping-basket fa-sm mx-1"></i>154 orders</span>
            <span class="text-success ms-2">In stock</span>
          </div> -->

          <div class="mb-3">
            <span class="h5">${{ product.price }}</span>
            <!-- <span class="text-muted">/per box</span> -->
          </div>

          <p>
           {{product.description}}
          </p>

          <!-- <div class="row">
            <dt class="col-3">Type:</dt>
            <dd class="col-9">Regular</dd>

            <dt class="col-3">Color</dt>
            <dd class="col-9">Brown</dd>

            <dt class="col-3">Material</dt>
            <dd class="col-9">Cotton, Jeans</dd>

            <dt class="col-3">Brand</dt>
            <dd class="col-9">Reebook</dd>
          </div> -->

          <hr />

          <div class="row mb-4">
            <!-- <div class="col-md-4 col-6">
              <label class="mb-2">Size</label>
              <select class="form-select border border-secondary" style="height: 35px;">
                <option>Small</option>
                <option>Medium</option>
                <option>Large</option>
              </select>
            </div> -->
            <!-- col.// -->
              <label class="mb-2 d-block">Quantidade</label>
              <div class="d-flex flex-row gap-2 h-14 text-center">
                <input 
                type="number" 
                class="form-control ml-2 px-4 py-2 border rounded-lg text-lg focus:outline-none focus:ring-2 focus:ring-blue-500" 
                style="width: 100px;"
                value="1"
                >  
                <router-link :to="`/checkout`" class="text-center btn" style="background: #00FF9C; width: 70%; height: 100%; align-content: center; font-size: larger; " @click="newpedido(product.id,userId)">comprar agora</router-link>     
              </div>
          </div>
        </div>
      </main>
    </div>
  </div>

  <div>
    <div class="d-flex justify-center flex-col items-center">
      <h1>Descrição</h1>

        <div v-html=" product.long_description " class="description" > </div>

    </div>
  </div>

          <cards :card=1 :text="'Compre tambem'"></cards>
</section> 
</template>

<script setup>
import { useRoute } from 'vue-router';
import cards from '../components/cards.vue';

import { onMounted, ref, nextTick } from 'vue';
import axios from 'axios';
import { decodeJwtPayload } from '../Services/decode-jwt';
const userId = ref(null);



const getImageUrl = (filename) => {
  return `${baseUrl}${filename}`;
};
const accessToken = ref(localStorage.getItem('token'));
const baseUrl = "http://127.0.0.1:5000/images/";
const route = useRoute(); // Captura os parâmetros da URL
// console.log("ID do Produto:", route.params.id);


  const products = ref([]);
  const fetchproducts = async () => {
    try {
      const response = await axios.get(`http://127.0.0.1:5000/products/listar-produtos/${route.params.id}`);
      products.value = [response.data];
      // console.log('response do servidor',response.data)
      // console.log('products value',products.value)
    } catch (error) {
      // console.error("Erro ao buscar produtos:", error);
    }
};

const newpedido = async (Product, User) => {
// console.log(Product,User)
  const response = await axios.post('http://127.0.0.1:5000/pedidos/newpedido', {
        pedido: [
        {
          Product: Product,
          User: User,
          Quant: 1,
        }
      ]
    });
      console.log(response)
    }
    
   
  
  onMounted(async () => {
    await fetchproducts(); // Garante que os produtos são carregados primeiro
    
    await nextTick();
    // console.log(accessToken)
    if (accessToken) {
      // console.log('teste')
      const payload = await decodeJwtPayload(accessToken.value);
      // Use a função importada
        if (payload && payload.sub) {
          userId.value = payload.sub;
        } else {
          console.log('Token inválido ou sem a claim "identity".');
        }
      } else {
        console.log('Nenhum token encontrado.');
      }// Espera o DOM ser atualizado antes de chamar o Slick
  })
</script>

<style>

.prod-card{
    transition: transform 0.3s;
}
<style>

h1{
  font-size: 2rem;
}
.prod-card:hover {
  transform: translateY(-5px);
}


.subimg{
  transition: transform 0.3s ease;
}


.subimg:hover {
  transform: scale(1.20); /* aumenta em 8% */
  }

  .description h3{
    font-size: 1.5rem
  }

  .description{
    text-align: center;
    margin-top: 20px;
  }

  .description table{
    margin: 0 auto;
    font-size: 1.1rem;
  }


  .description h2{
    font-size: 1.3rem
  }

  .description .product-description{
    display: flex;
    flex-direction: column;
    gap: 20px;
  }

  .description table {
        width: 100%;
        border-collapse: collapse;
        margin: 20px 0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        box-shadow: 0 2px 3px rgba(0,0,0,0.1);
    }
    
    .description table th {
        background-color: #2c3e50;
        color: white;
        text-align: left;
        padding: 12px;
    }
    
    .description table td {
        padding: 10px 12px;
        border-bottom: 1px solid #e0e0e0;
    }
    
    .description table tr:nth-child(even) {
        background-color: #f8f9fa;
    }
    
    .description table tr:hover {
        background-color: #f1f1f1;
    }
</style>
