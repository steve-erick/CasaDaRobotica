<template>
    <div class="flex p-4 flex-column justify-center mt-24">
            <!-- Adicione a classe 'slicker' para o Slick -->
                
                <h1 class="self-center text-3xl">{{props.text}}</h1>
                <div class="slicker">
                    <div class="me-2 card custom-shadow border-0" v-for="(product, i) in products" :key="i">
                        <img :src="product.src" loading="lazy" class="card-img-top" alt="Imagem do produto">
                        <div class="card-body">
                            <h5 class="card-text m-0">R${{ product.price }}</h5>
                            <p class="card-text text-sm">{{ product.name }}</p>
                            <div class="flex justify-center gap-2">
                              <router-link :to="`/product/${product.id}`" class="text-center buttons btn" style="background: #00FF9C;">Ver mais</router-link>     
                              <button @click="newpedido(product.id,userId)" class="text-center buttons btn ml-2 " style="background: #4efcfc;"><i class="bi-cart"></i>Adicionar</button>                                         
                            </div>
                          </div>
                    </div>
                </div> 
      </div>   

      <div v-if="showModal" class="modal fade show" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true" style="display: block;">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Confirmar Remoção</h5>
            <button type="button" class="btn-close" id="FecharButton"@click="closeModal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            Tem certeza de que deseja remover este item?
            <p>{{ pedido }}</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" id="cancelarButton" @click="closeModal">Cancelar</button>
            <button type="button" class="btn btn-danger" @click="removePedido(itemToRemove)">Remover</button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import $ from 'jquery';
  import axios from 'axios';
  import { onMounted, ref, nextTick } from 'vue';
  import { RouterLink } from 'vue-router';
  import { decodeJwtPayload } from '../Services/decode-jwt';
  
  const props = defineProps({
  card: {
    type: Number,
    default: 0, // Exemplo: 'light' ou 'dark'
    },
  text: {
    type: String,
    default: "Mais vendido",
  }
});

  const products = ref([]);
  const accessToken = ref(localStorage.getItem('token'));
  const userId = ref(null);
  const specialcode = props.card
  const fetchproducts = async () => {
    
    try {
      const response = await axios.get("http://127.0.0.1:5000/products/listar-produtos");
      products.value = response.data.products.filter(product => product.special === specialcode);
      console.log(products.value)
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
    await fetchproducts(); 
    await nextTick(); 
    
  await import('slick-carousel')
  await import ('slick-carousel/slick/slick.css');
  await import ('slick-carousel/slick/slick-theme.css');

  await import('jquery-mask-plugin')

  // inicialize o slick-carousel (exemplo)
  $('.seletor-do-slick').slick({
    // opções aqui
  })
    if (accessToken) {
        const payload = await decodeJwtPayload(accessToken.value); // Use a função importada
        if (payload && payload.sub) {
          userId.value = payload.sub;
        } else {
          console.log('Token inválido ou sem a claim "identity".');
        }
      } else {
        console.log('Nenhum token encontrado.');
      }

    
  
    setTimeout(() => {
      $(".slicker").slick({
        slidesToShow: 5, 
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 2000,
        arrows: false,
        dots: true,
        responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 3,
      }
    },
    {
      breakpoint: 768,
      settings: {
        slidesToShow: 2,
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
      }
    }
  ]
      });
    }, 500);

    
  });
  

  </script>
  
  <style>
  /* Certifique-se de que o Slick está formatado corretamente */
  .slick-slide {
    padding: 10px;
  background: transparent !important;
  overflow: visible !important;

  }
.slicker {
  background-color: #f4f6f8; /* ou #f0f0f0 */
  padding: 20px 0;
}

  .slick-list {
  overflow: hidden;
}

.slick-track {
  display: flex;
  overflow: hidden;
}

.card-img-top {
  width: 100% ;
  height: 200px;
  object-fit: contain;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;

}

.buttons{
 font-size: 0.9rem;
}
.custom-shadow {
  border-radius: 12px;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.12);
  transition: all 0.3s ease-in-out;
  background-color: white;
}

.custom-shadow:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 28px rgba(0, 0, 0, 0.18);
}

.card-body h5 {
  font-weight: 600;
  font-size: 1.1rem;
}

.card-body p {
  font-size: 0.9rem;
  color: #555;
}
  </style>
  