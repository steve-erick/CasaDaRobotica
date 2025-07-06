<template>
      <div v-if="products.length === 0" class="text-center p-2">
  <p>Nenhum produto encontrado</p>
</div>

      <div  v-else class="d-flex flex-col justify-center items-center p-2">            
                  <div v-for="(product, i) in products" :key="i" class="card mb-3" style="width: 80%;">
                  <div class="row g-0">
                        <div class="col-md-4 " style="width: 200px;">
                              <img :src=product.src class="img-fluid rounded-start" alt="..." style="height: 200px; width: 200px;">
                        </div>
                              <div class="col-md-8 d-flex align-items-center justify-content-center">
                                    <div class="card-body flex flex-col p-2 gap-1">
                                                <h5 class="card-title m-0 text-xl">{{product.name}}</h5>
                                                <p class="card-text m-0 p-0">{{ product.description }}</p>
                                                <h4 class=" text-xl fw-bold >" style="color: #00FF9C;">R$ {{ product.price }}</h4>
                                          <div class="d-flex gap-2">
                                                <router-link :to="`/product/${product.id}`" class="text-center btn" style="background: #00FF9C;">Ver mais</router-link>     
                                                <button @click="newpedido(product.id,userId)" class="text-center btn ml-2 " style="background: #4efcfc;"><i class="bi-cart"></i>Adicionar</button>                                         
                                          </div>
                                    </div>
                              </div>
                        </div>
                  </div> 
            </div>
            
</template>

<script setup>
import { useRoute } from 'vue-router';
import axios from 'axios';
import { onMounted, ref, nextTick } from 'vue';
import { watch } from 'vue';

const products = ref([])

const route = useRoute(); // Captura os parâmetros da URL
console.log("Name:", route.params.name);

const fetchproducts = async () => {
    try {
          const response = await axios.get(`http://127.0.0.1:5000/products/search`, {
            params: {
            search: route.params.name
            }
          });
          products.value = response.data.products;
          console.log(products.value.length)
      console.log('response do servidor',response.data)
      console.log('products value',products.value)
    } catch (error) {
      console.error("Erro ao buscar produtos:", error);
    }
};


const newpedido = async (Product, User) => {
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
})

watch(() => route.params.name, async (newName, oldName) => {
  console.log("Rota mudou de:", oldName, "para:", newName);
  await fetchproducts();
});
</script>