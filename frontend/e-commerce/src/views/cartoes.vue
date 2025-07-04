<template>

<div class="bg-light">
    <div class="container py-5">
        <div class="row">

            <!-- Main Content -->
            <div class="col-12">
                <div class="card border-0 shadow-sm">
                    <div class="card-body p-0">
                        <div class="row g-0">
                            <!-- Sidebar -->
                            <div class="col-lg-3 border-end">
                                <div class="p-4">
                                    <div class="nav flex-column nav-pills">
                                        <router-link :to="`/controlpanel/`" class="nav-link"><i class="fas fa-user me-2"></i>Minha conta</router-link>
                                        <router-link :to="`/controlpanel/pedidos/`" class="nav-link"><i class="bi bi-clipboard me-2"></i>Pedidos</router-link>
                                        <router-link :to="`/controlpanel/cartoes/`" class="nav-link active"><i class="fas fa-credit-card me-2"></i>Meus cartões</router-link>
                                    </div>
                                </div>
                            </div>

                            <!-- Content Area -->
                            <div class="col-lg-9">
                                <div class="p-4">
                                 

                                    <table style="width: 100%;">
                                        <thead>
                                            <tr>
                                                <th>Card</th>
                                                <th>Num</th>
                                                <th>CVV</th>
                                                <th>Data</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                <tr
                  v-for="(Card, i) in Cards"
                  :key="i"
                  class="bg-white shadow-md rounded-lg border mb-4"
                >
                  <td>
                    <img
                      :src="getImageUrl(Card.CardType)"
                      alt="Card Image"
                      style="width: 70px; height: 70px;" loading="lazy"
                    />
                  </td>
                  <td>
                    {{ maskedRows[i] ? maskValue(realCardValues[i]?.Num) : realCardValues[i]?.Num }}
                  </td>
                  <td>
                    {{ maskedRows[i] ? maskValue(realCardValues[i]?.CVV) : realCardValues[i]?.CVV }}
                  </td>
                  <td>{{ Card.Mes }}/{{ Card.Ano }}</td>
                  <td>
                    <div class="flex gap-2 justify-center">
                      <i
                        :class="[
                          'bi',
                          maskedRows[i] ? 'bi-eye' : 'bi-eye-slash',
                          'text-2xl',
                          'cursor-pointer'
                        ]"
                        @click="toggleMask(i)"
                      ></i>
                      <i
                        class="bi bi-trash text-2xl cursor-pointer"
                        @click="deleteCard(Card.id)"
                      ></i>
                    </div>
                  </td>
                </tr>
              </tbody>
                    
                                    </table>
                                    <div class="d-flex justify-content-center align-items-center flex-column mt-4 cursor-pointer" data-bs-toggle="modal" data-bs-target="#exampleModal">

                                       <img
                      :src="getImageUrl('square-icon')"
                      alt="Card Image"
                      style="width: 80px; height: 80px;" class="margin-0 " loading="lazy"
                    />

                    <h5 class="justify-self-center">adicione um novo cartão</h5>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </div>
</div>
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">

  <div class="modal-dialog">
    <div class="modal-content">
      
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Adicionar novo cartão</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Fechar"></button>
      </div>

      <div class="modal-body">
        <form>
          <div class="mb-3">
            <label for="numeroCartao" class="form-label">Número do Cartão</label>
            <input type="text" class="form-control" id="numeroCartao" placeholder="1234 5678 9012 3456">
          </div>
          <div class="mb-3">
            <label for="cvv" class="form-label">CVV</label>
            <input type="text" class="form-control" id="cvv" placeholder="123">
          </div>
          <div class="mb-3">
            <label for="validade" class="form-label">Validade</label>
            <input type="month" class="form-control" id="validade">
          </div>
        </form>
      </div>

      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
        <button type="button" class="btn btn-primary">Salvar</button>
      </div>

    </div>
  </div>
</div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { decodeJwtPayload } from '../Services/decode-jwt';
import { useRouter } from 'vue-router';

const accessToken = ref(localStorage.getItem('token'));
const Cards = ref([]);
const userId = ref(null);
const router = useRouter();
const maskedRows = ref([true,true,true]);  // Estado de cada linha (true = mascarado)
const realCardValues = ref({});  // Valores reais de Num e CVV

const CardsData = async () => {
    try {
        const response = await axios.get(`http://127.0.0.1:5000/Cards/${userId.value}`);
        Cards.value = response.data.Cards;

        // Salvar os valores reais de Num e CVV
        realCardValues.value = {};
        Cards.value.forEach((card, index) => {
            realCardValues.value[index] = {
                Num: card.Num,
                CVV: card.CVV
            };
        });
    } catch (error) {
        console.error("Erro ao buscar dados do usuario:", error);
    }
};

onMounted(async () => {
    if (accessToken.value) {
          const payload = await decodeJwtPayload(accessToken.value);
          if (payload && payload.sub) userId.value = payload.sub;
        }else{
          router.push('/sign-in')
        }
    await CardsData();
});

const baseUrl = "http://127.0.0.1:5000/images/";

const getImageUrl = (filename) => {
    return `${baseUrl}${filename}.webp`;
};

const maskValue = (value) => {
  if (!value) return '';
  return '*'.repeat(value.length);
};

const toggleMask = (index) => {
  maskedRows.value[index] = !maskedRows.value[index];
};


const viewCard = (card) => {
    console.log('Ver:', card);
};

const deleteCard = (id) => {
    console.log('Deletar:', id);
};
</script>

<style>
.nav-pills .nav-link.active {
    background-color: #2CA7B8;
    color: white;
}

.nav-pills .nav-link {
    color: #2CA7B8;
}

.nav-pills .nav-link:hover {
    color: #00C896;
}
</style>
