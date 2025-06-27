  <template>  
    <nav class="navbar bg-robotic-blue border-body" style="background-color: #2CA7B8;">
      <div class="container-fluid">
        <router-link :to="`/`" class="w-12 cursor-pointer"><img src="../assets/logo.png" alt=""></router-link>
        <form @submit.prevent="handleSubmit" class="d-flex flex-initial w-1/2 " role="search">
          <input v-model="search" class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
          <button class="search-button w-24 rounded-2 border-1 border-white" type="submit" style=" color: white; border: 0;">Search</button>
        </form>
    
        <div class="flex flex-col text-center">
          <div v-if="!isLoadingAuth"> 
            <div v-if="auth == 'Authenticated'">
              <li class="nav-item dropdown list-none" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            <a class="bi bi-person-circle text-white text-4xl hover:text-white"> </a>
            <p class="text-white mb-0">{{ userName }}</p>  
            
            <ul class="dropdown-menu" data-bs-theme="dark"  >
            <li><a @click="router.push('/controlpanel')" class="dropdown-item" >Painel de controle</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a @click="router.push('/controlpanel/pedidos')" class="dropdown-item" >Pedidos</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#" @click="sairUser">Sair</a></li>
          </ul>
        </li> 
          
          </div>
    
          <div v-else>
            <a class="bi bi-person-circle text-white text-4xl hover:text-white"> </a>
            <div class="d-flex flex-row text-center text-white ">
              <router-link :to="`/sign-in/`" class="no-underline text-inherit text-sm m-0 hover:text-robotic-green  cursor-pointer">LOGIN</router-link>
              <router-link :to="`/sign-up/`"  class="no-underline  text-inherit pl-2 m-0 text-sm hover:text-robotic-green cursor-pointer">CADASTRO</router-link>
            </div>
          </div>
        </div>
        <div v-else>
          <p class="text-white text-sm">Verificando autenticação...</p>
        </div>
          </div>
    
    
        <a class="cart-icon border-1 rounded-md navbar-toggler border-white cursor-pointer" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar" aria-controls="offcanvasNavbar" aria-label="Toggle navigation"  @click="fetchpedidos">
          <i class="bi bi-cart p-2 text-white text-2xl hover:text-white"></i>
        </a>
        <div class="offcanvas offcanvas-end" data-bs-theme="dark" tabindex="-1" id="offcanvasNavbar" aria-labelledby="offcanvasNavbarLabel">
          <div class="offcanvas-header">
            <h5 class="offcanvas-title" id="offcanvasNavbarLabel">Carrinho</h5>
            <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
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
            <div class="card p-2 " v-if="pedido.Status == 'Pending'" style="max-height: 200px; overflow-y: auto;">
              <div class="flex flex-row">
                <img :src="pedido.Product.src" class="img-thumbnail" style="width: 150px; height: 130px;" alt="Imagem do produto">
                <div class="flex flex-col">
                  <p class="mb-0 p-2 text-sm">{{ pedido.Product.name }}</p>
                  <input 
                    type="number" 
                    class="form-control ml-2 px-4 py-2 border rounded-lg text-lg focus:outline-none focus:ring-2 focus:ring-blue-500" 
                    placeholder="Digite um número" 
                    v-model="pedido.Amount"   
                    style="width: 100px;"
                    @change="AttAmount($event,pedido.pedido_id)"
                  >          
                  <router-link :to="`/checkout`" class="btn mt-3 ml-2 text-black" style="background: #00FF9C;">finalizar pedido</router-link>
                </div>
                <!-- X button to remove the item -->
                <button 
                  class="btn btn-sm btn-danger ml-2" 
                  @click="openModal(i,pedido.pedido_id)" 
                  style="border-radius: 50%; padding: 5px; width: 30px; height: 30px; color: white; font-size: 18px; display: flex; justify-content: center; align-items: center;"
                >
                  X
                </button>
              </div>
            </div>
    </div>
    <div v-if="pedidos.length > 3" class='flex items-center justify-center'>
      <button @click="setpedidosindex()" class="btn mt-3 ml-2 text-black mb-1" style="background: #00FF9C; width: 25%;">Próximo</button> 
    </div>
    
    
        </div>
      </div>
    </nav>
    </template>
    
    <script setup>
    import { ref, onMounted } from 'vue'; // 1. Importe 'ref' de 'vue'
    import { autentication } from '../Services/autentication' 
    import { decodeJwtPayload } from '../Services/decode-jwt';
    import axios from 'axios';
    import { nextTick } from 'vue';
    // import Product from '../views/product.vue';
    import { useRouter } from 'vue-router' // <== Adicione isso

  const router = useRouter()
  const search = ref('')
    const auth = ref(null);
    const isLoadingAuth = ref(true); // Nova flag de carregamento
    const accessToken = ref(localStorage.getItem('token'));
    const userId = ref(null);
    const userName = ref(null)
    const datafromuser = ref([])
    const pedidos = ref([])
    const pedidosindex = ref(0)
    // const limitedpedidos = ref([])
    const limit = ref(3)
    const pedidoslength = ref()
    // await userdata()
    
    const showModal = ref(false); // To control the modal visibility
    const itemToRemove = ref(null); // To store the item index to remove
    const indexToRemove = ref(null)

    
    // Open the modal and store the index of the item to be removed

    const handleSubmit = () => {
  if (search.value.trim()) {
    // Redireciona para a rota com o parâmetro
    router.push(`/search/${encodeURIComponent(search.value)}`)
  }
}
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

    const sairUser = () => {
      localStorage.removeItem("token")
      location.reload();
    }
    
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
    
    
    onMounted(async () => {
      try {
        if (accessToken.value) {
        const isAuthenticated = await autentication();
        console.log(isAuthenticated)
        auth.value = isAuthenticated.ok ? 'Authenticated' : null;    
        console.log(auth.value)
        const payload = await decodeJwtPayload(accessToken.value);
          if (payload && payload.sub) userId.value = payload.sub;
        }else{
          // router.push('/sign-in')
        }
      } catch (error) {
        console.error('Erro ao verificar autenticação:', error);
        auth.value = null;
      } finally {
        isLoadingAuth.value = false; // Define como false após a conclusão (sucesso ou falha)
      }
      await userdata();
      await fetchpedidos();

      
    });
    
    
    const userdata = async () => {
      try {
        if(accessToken.value){

          const response = await axios.get(`http://127.0.0.1:5000/users/get-user/${userId.value}` , {
            headers: {
              'Authorization': ' `Bearer ${accessToken}`',
            }
          });
          // console.log(userId.value)
          // console.log('data', response.data)
          datafromuser.value = [response.data];   
          // console.log('datafromuser:', datafromuser.value[0].name); 
          userName.value = datafromuser.value[0].name
          // console.log('Name',userName.value)
        }else{
          console.log(userId.value,'userid')
        }
        } catch (error) {
          console.error("Erro ao buscar dados do usuario:", error);
      }
    }

    
    
    const fetchpedidos = async () => {
      try {
        // if(userId.value =! 'undefined'){
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
        // }else{
        //   console.log('não esta logado')
        // }
        } catch (error) {
          console.error("Erro ao buscar pedidos:", error);
        }
      };
    
      const limitedpedidos = () => {
      // return pedidos.value.slice(init, end);
        const start = pedidosindex.value;
      // console.log(start)
      const end = start + limit.value;
      
      return pedidos.value.slice(start, end);

      };

    const setpedidosindex = () => {
      if (pedidosindex.value >= pedidoslength.value) {
        console.log('caiu aqui')
        pedidosindex.value = 0
      } else {
        pedidosindex.value += 3
        if (pedidosindex.value >= pedidoslength.value) {
          pedidosindex.value = 0
        }
        }
      }

      </script>
    
    
    <style>
.cart-icon {
    background-color: #2CA7B8; /* ou qualquer cor inicial */
  }

  .cart-icon:hover{
    background-color: rgb(5, 221, 167);
    transition: background-color 0.3s;
  }

  .search-button{
    background-color: #00C896;
  }
  .search-button:hover{
    background-color: rgb(5, 221, 167);
    transition: background-color 0.3s;
  }
  </style>