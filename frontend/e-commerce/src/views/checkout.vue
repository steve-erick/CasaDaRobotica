<template>

    <section class="h-100 h-custom" >
  <div class="container py-5 h-100">
    <div class="row d-flex justify-content-center align-items-center h-100">
      <div class="col">
        <div class="card">
          <div class="card-body p-4">

            <div class="row">

              <div class="col-lg-7">
                <h5 class="mb-3"><router-link :to="`/`" to href="#!" class="text-body no-underline"><i
                      class="fas fa-long-arrow-alt-left me-2"></i>Volte as compras</router-link></h5>
                <hr>

                <div class="d-flex justify-content-between align-items-center mb-4">
                  <div>
                    <p class="mb-0">Você tem {{ pedidos.length }} items no seu carrinho</p>
                  </div>
                </div>

                <div v-for="(pedido, i) in limitedpedidos()" :key="i">

                    <div class="card mb-3">
                        <div class="card-body">
                    <div class="d-flex justify-content-between">
                      <div class="d-flex flex-row align-items-center">
                        <div>
                          <img
                            :src="pedido.Product.src"
                            class="img-fluid rounded-3" alt="Shopping item" style="width: 65px;" loading="lazy">
                        </div>
                        <div class="ms-3">
                          <h5>{{ pedido.Product.name }}</h5>
                        </div>
                      </div>
                      <div class="d-flex flex-row align-items-center">
                          <div style="width: 50px;">
                              <h5 class="fw-normal mb-0">{{ pedido.Amount }}</h5>
                        </div>
                        <div style="width: 100px;">
                          <h5 class="mb-0 me-2" style="font-size: 1.2rem">R${{ pedido.Product.price }}</h5>
                        </div>
                        <button type="button" class="btn btn-outline-danger me-2 " @click="openModal(i,pedido.pedido_id)" >
                            <i class="bi bi-trash"></i>
                        </button>
                    
                    </div>
                </div>
            </div>
        </div>
        
    </div>

                                 <div v-if="pedidos.length > 5" class='flex justify-center'> 
                                 <button @click="setpedidosindex()" class="btn mt-3 ml-2 text-black mb-1" style="background: #00FF9C; width: 25%;">Próximo</button>  
                                </div>
              </div>
              <div class="col-lg-5">

                <div class="card text-white rounded-3" style="background-color: #00C896;">
                  <div class="card-body">
                    <div class="d-flex justify-content-between align-items-center mb-4">
                      <h5 class="mb-0">Detalhes do Cartão</h5>

                    </div>

                    <div class="flex gap-2">
                 <div>
                  
                </div> 
                <div @click="selectCard('mastercard')" class="cursor-pointer">
                  <i v-if="card !== 'mastercard'" class="fab fa-cc-mastercard fa-3x me-2 "></i>
                  <i v-else class="fab fa-cc-mastercard fa-4x me-2 text-robotic-green"></i>
                </div>

                <!-- Visa -->
                <div @click="selectCard('visa')" class="cursor-pointer">
                  <i v-if="card !== 'visa'" class="fab fa-cc-visa fa-3x me-2 "></i>
                  <i v-else class="fab fa-cc-visa fa-4x me-2 text-robotic-green"></i>
                </div>

                <!-- Paypal -->
                <div @click="selectCard('paypal')" class="cursor-pointer">
                  <i v-if="card !== 'paypal'" class="fab fa-cc-paypal fa-3x me-2 "></i>
                  <i v-else class="fab fa-cc-paypal fa-4x me-2 text-robotic-green"></i>
                </div>
                    </div>
                    <form class="mt-10">
                      <div data-mdb-input-init class="form-outline form-white mb-4">
                        <input type="text" id="typeName" class="form-control form-control-lg" siez="17"
                          placeholder="Nome no Cartão" />
                        <label class="form-label" for="typeName">Nome no Cartão</label>
                      </div>

                      <div data-mdb-input-init class="form-outline form-white mb-4">
                        <input type="text" id="typeText" class="form-control form-control-lg" siez="17"
                          placeholder="1234 5678 9012 3457" minlength="19" maxlength="19" />
                        <label class="form-label" for="typeText">Número do Cartão</label>
                      </div>

                      <div class="row mb-4">
                        <div class="col-md-6">
                          <div data-mdb-input-init class="form-outline form-white">
                            <input type="text" id="typeExp" class="form-control form-control-lg"
                              placeholder="MM/YYYY" size="7" minlength="7" maxlength="7" />
                            <label class="form-label" for="typeExp">Validade</label>
                          </div>
                        </div>
                        <div class="col-md-6">
                          <div data-mdb-input-init class="form-outline form-white">
                            <input type="password" id="typeText" class="form-control form-control-lg"
                              placeholder="&#9679;&#9679;&#9679;" size="1" minlength="3" maxlength="3" />
                            <label class="form-label" for="typeText">Cvv</label>
                          </div>
                        </div>
                      </div>

                    </form>

                    <hr class="my-4">

                    <div class="d-flex justify-content-between text-white">
                      <p class="mb-2">Subtotal</p>
                      <p class="mb-2">{{ totalComQuantidade }}</p>
                    </div>

                    <div class="d-flex justify-content-between text-white">
                      <p class="mb-2">Frete</p>
                      <p class="mb-2">$20.00</p>
                    </div>

                    <div class="d-flex justify-content-between mb-4 text-white">
                      <p class="mb-2">Total(Incl. taxes)</p>
                      <p class="mb-2">{{ totalComQuantidade + 20 }}</p>
                    </div>

                    <button  type="button" data-mdb-button-init data-mdb-ripple-init class="btn btn-info btn-block btn-lg">
                      <div class="d-flex justify-content-between">
                        <span class="text-white">Finalizar <i class="bi bi-bag-check ms-2 text-white"></i></span>
                      </div>
                    </button>

                  </div>
                </div>

                
              </div>

            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

   <div v-for="(pedido, i) in limitedpedidos()" :key="i" class="offcanvas-body">

            
    <div v-if="showModal" class="modal fade show" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true" style="display: block;">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Confirmar Remoção</h5>
            <button type="button" class="btn-close" id="FecharButton"@click="closeModal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            Tem certeza de que deseja remover este item?
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" id="cancelarButton" @click="closeModal">Cancelar</button>
            <button type="button" class="btn btn-danger" @click="removePedido(itemToRemove)">Remover</button>
          </div>
        </div>
      </div>
    </div>
   </div>
</section>
</template>

<script setup >
import axios from 'axios';
import { onMounted, ref ,computed,nextTick} from 'vue';
import { decodeJwtPayload } from '../Services/decode-jwt';

const pedidos = ref([])
const pedidoslength = ref()
const accessToken = ref(localStorage.getItem('token'));
const userId = ref()
const limit = ref(5)
const showModal = ref(false); // To control the modal visibility
const itemToRemove = ref(null); // To store the item index to remove
const indexToRemove = ref(null)
const pedidosindex = ref(0)
const card = ref()
const totalComQuantidade = computed(() => {
  if (!pedidos.value || pedidos.value.length === 0) return 0;

  const total = pedidos.value.reduce((soma, pedido) => {
    const preco = pedido.Product?.price || 0;
    const quantidade = pedido.Amount || 1;
    return soma + (preco * quantidade);
  }, 0);

  // Arredonda para 2 casas decimais
  return total.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
});


const selectCard = (cardName) => {
  card.value = cardName;
};
 const AttAmount = async (event, id) => {
      if (event.target.value > 0) { 
        const response = await axios.get(`http://127.0.0.1:5000/pedidos/${id}/Amount` , {
          headers: {
            'Authorization': ' `Bearer ${accessToken}`',
            'Amount': `${event.target.value}`
          }
        });
        console.log(response)
      }
    
      // console.log(response)
      else if (event.target.value <= 0) {
        event.target.disabled = true;
        await openModal(); // espera o usuário fechar
        event.target.disabled = false;
        event.target.value = 1; // corrige
        const response = await axios.get(`http://127.0.0.1:5000/pedidos/${id}/Amount` , {
          headers: {
            'Authorization': ' `Bearer ${accessToken}`',
            'Amount': 1
          }
        });
        console.log(response)
      }
};

const openModal = async (index,id) => {
      itemToRemove.value = id;
      indexToRemove.value = index;
      // console.log(id)
      // console.log(index)
      showModal.value = true;
      await nextTick(); // ESPERA o Vue montar o DOM
    
      return new Promise((resolve) => {
        const close = () => {
          showModal.value = false;
          resolve();
        };
    
        document.getElementById('cancelarButton').onclick = close;
        document.getElementById('FecharButton').onclick = close;
      });
    };
    
    // Close the modal
    const closeModal = () => {
      showModal.value = false;
    };
    
    // Remove the item from the pedidos array
    const removePedido = (id) => {
        // console.log(id)
        const response = axios.get(`http://127.0.0.1:5000/pedidos/${id}/remover`);
      console.log(response)
        // console.log(indexToRemove)
        pedidos.value.splice(indexToRemove.value, 1); 
        itemToRemove.value = null;
        indexToRemove.value = null
        closeModal();
    }
    
const fetchpedidos = async () => {
    try {
        // if (auth.ok) {
          const response = await axios.get(`http://127.0.0.1:5000/pedidos/listar-pedidos/${userId.value}`);
          pedidos.value = response.data.pedidos;
          pedidoslength.value = pedidos.value.length;
          console.log(pedidoslength.value)
          console.log('pedidos.value',pedidos.value)  
          console.log('response',response.data.pedidos)
        // }
        // else {
        //   pedidos.value = 'Não há pedidos'
        //   }
        } catch (error) {
          console.error("Erro ao buscar pedidos:", error);
        }
};

const limitedpedidos = () => {
    // return pedidos.value.slice(init, end);
      
        const start = pedidosindex.value;
      // console.log(start)
      const end = start + limit.value;
      
    //   console.log('pedidos.value.slice(start, end))
      return pedidos.value.slice(start, end);
      };

    const setpedidosindex = () => {
      if (pedidosindex.value >= pedidoslength.value) {
        console.log('caiu aqui')
        pedidosindex.value = 0
      } else {
        pedidosindex.value += 5
        if (pedidosindex.value >= pedidoslength.value) {
          pedidosindex.value = 0
        }
        }
}
      
onMounted(async () => {
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
        
      await fetchpedidos()  
    })
</script>