<template>
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">

  <div class="bg-light">
    <div class="container py-5">
      <div class="row" style="background-color: white;">
        <!-- Sidebar -->
        <div class="col-lg-3 border-end">
          <div class="p-4">
            <div class="nav flex-column nav-pills">
              <router-link :to="`/controlpanel/`" class="nav-link">Minha conta</router-link>
              <router-link :to="`/controlpanel/pedidos/`" class="nav-link active">Pedidos</router-link>
              <router-link :to="`/controlpanel/cartoes/`" class="nav-link">Meus cartões</router-link>
              <router-link :to="`/controlpanel/atividade/`" class="nav-link">Atividade</router-link>
            </div>
          </div>
        </div>

        <!-- Content -->

        <div class="col-lg-9">
          <div class="p-4">
              <div v-if="userpedidos.length > 0">
            <!-- Lista de Pedidos -->
            <div class=" p-2">
                    <div class="flex gap-2">
                        <button @click="setpedidosindex()" class="btn btn-outline-info" >Entregues</button> 
                        <button @click="setpedidosindex()" class="btn btn-outline-info" >Em Tránsito</button> 
                    </div>

              <div v-for="(pedido, i) in userpedidos" :key="i" class="p-2">
                <div class="card rounded-lg p-2 flex flex-row items-center">
                  <img :src="pedido.Product.src" alt="" style="width: 100px; height: 100px;">
                  <div class="flex flex-col p-3">
                    <h4>{{ pedido.Product.name }}</h4>
                    <p>${{ pedido.Product.price }}</p>
                  </div>
                </div>
              </div>
              <div class="flex justify-center" v-if="userpedidos.length > 4">
                  <button @click="setpedidosindex()" class="btn mt-3 ml-2 text-black mb-1" style="background: #00FF9C; width: 10%;">Próximo</button> 
                </div>

            </div>

            <!-- Gráfico Polar -->
            <div class="mt-4">
              <PolarArea :data="chartData" :options="chartOptions" />
            </div>
          </div>

          <div v-else>
            <div class="">
              <h4>Sem pedidos registrados</h4>
            </div>
          </div>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { decodeJwtPayload } from '../Services/decode-jwt';
import { ref, onMounted } from 'vue';
import { PolarArea } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, RadialLinearScale, ArcElement } from 'chart.js';
import { useRouter } from 'vue-router';
// Registrar componentes necessários para PolarArea
ChartJS.register(Title, Tooltip, Legend, RadialLinearScale, ArcElement);

const accessToken = ref(localStorage.getItem('token'));
const userId = ref();
const userpedidos = ref([]);
const router = useRouter()


// Chart Data
const chartData = ref({
  labels: ['Motores', 'Sensores', 'Placas'],
  datasets: [{
    label: 'Pedidos por Categoria',
    data: [0, 0, 0],
    backgroundColor: ['#3498db', '#2ecc71', '#e74c3c']
  }]
});

const chartOptions = {
  responsive: true,
  plugins: {
    legend: {
      position: 'top'
    },
    title: {
      display: true,
      text: 'Produtos mais comprados'
    }
  }
};

// Buscar Pedidos
const pedidos = async () => {
  try {
    if(userId.value == undefined){
      console.log('Não esta logado')
  }else{
    const response = await axios.get(`http://127.0.0.1:5000/pedidos/listar-pedidos/${userId.value}`);
      userpedidos.value = response.data.pedidos.filter(p => p.Status === "Completed");
      
    console.log("Pedidos filtrados:", userpedidos.value);

    const categorias = { Motores: 0, Sensores: 0, Placas: 0 };
    
    userpedidos.value.forEach(p => {
      const desc = (p.Product.description || '').toLowerCase();
      if (desc.includes('motor')) categorias.Motores++;
      else if (desc.includes('sensor')) categorias.Sensores++;
      else categorias.Placas++;
    });

    console.log("Contagem por categoria:", categorias);

    chartData.value = {
      ...chartData.value,
      datasets: [{
        ...chartData.value.datasets[0],
        data: [categorias.Motores, categorias.Sensores, categorias.Placas]
      }]
    };
  } 

  } catch (error) {
    console.error("Erro ao buscar pedidos:", error);
  }
};

onMounted(async () => {
  if (accessToken.value) {
    const payload = await decodeJwtPayload(accessToken.value);
    if (payload && payload.sub) userId.value = payload.sub;
  }else{
    router.push('/sign-in')
  }
  console.log(userId.value)
  await pedidos();
});
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
