<template>

<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">

<div class="bg-light">
    <div class="container py-5">
        <div class="row">
            <!-- Profile Header -->
            <!-- <div class="col-12 mb-4">
                
                <div class="text-center">
                    <div class="position-relative d-inline-block">
                        <img src="https://randomuser.me/api/portraits/men/40.jpg" class="rounded-circle profile-pic" alt="Profile Picture">
                        <button class="btn btn-primary btn-sm position-absolute bottom-0 end-0 rounded-circle">
                            <i class="fas fa-camera"></i>
                        </button>
                    </div>
                    <h3 class="mt-3 mb-1">Alex Johnso</h3>
                   
                </div>
            </div> -->

            <!-- Main Content -->
            <div class="col-12">
                <div class="card border-0 shadow-sm">
                    <div class="card-body p-0">
                        <div class="row g-0">
                            <!-- Sidebar -->
                            <div class="col-lg-3 border-end">
                                <div class="p-4">
                                    <div class="nav flex-column nav-pills " >
                                         <router-link :to="`/controlpanel/`" class="nav-link active"  href="#"><i class="fas fa-user me-2"></i>Minha conta</router-link >
                                        <router-link :to="`/controlpanel/pedidos/`" class="nav-link" href="#"><i class="bi bi-clipboard me-2"></i>Pedidos</router-link >
                                        <router-link :to="`/controlpanel/cartoes/`" class="nav-link" href="#"><i class="fas fa-credit-card me-2"></i>Meus cartões</router-link >
                                        </div>
                                </div>
                            </div>

                            <!-- Content Area -->
                            <div class="col-lg-9">
                                <div class="p-4">
                                    <!-- Personal Information -->
                                    <div class="mb-4">
                                        <h5 class="mb-4">Personal Information</h5>
                                        <div class="row g-3" v-for="(user, i) in datafromuser" :key="i">
                                            <div class="col-md-6">
                                                <label class="form-label">First Name</label>
                                                <input type="text" class="form-control"  :value="user.name.split(' ')[0]">
                                            </div>
                                            <div class="col-md-6">
                                                <label class="form-label">Last Name</label>
                                                <input type="text" class="form-control" :value="user.name.split(' ').slice(1).join(' ')">
                                            </div>
                                            <div class="col-md-6">
                                                <label class="form-label">Email</label>
                                                <input type="email" class="form-control" :value="user.email">
                                            </div>
                                            <div class="col-md-6">
                                                <label class="form-label">Phone</label>
                                                <input id="phone" type="tel" class="form-control" :value="user.phone">
                                            </div>
                                        </div>
                                    </div>

                                 
                                    <button type="button" class="btn btn-primary">Salvar</button>
                                    <!-- Recent Activity -->
                                    <div>
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
</template>

<script setup>
import { ref, onMounted,nextTick } from 'vue'
import { decodeJwtPayload } from '../Services/decode-jwt';
import axios from 'axios';
import { useRouter } from 'vue-router';
import $ from 'jquery';
import 'jquery-mask-plugin';

const accessToken = ref(localStorage.getItem('token'));
const datafromuser = ref([])
const userId = ref();
const router = useRouter()

 const userdata = async () => {
      try {        
        const response = await axios.get(`http://127.0.0.1:5000/users/get-user/${userId.value}` , {
          headers: {
            'Authorization': ' `Bearer ${accessToken}`',
            }
        });
        // console.log('data', response.data)
        datafromuser.value = [response.data];   
        // console.log('Name',userName.value)

         await nextTick();

    // Só agora o input existe no DOM
    $('#phone').mask('(00) 00000-0000')
      } catch (error) {
        console.error("Erro ao buscar dados do usuario:", error);
      }
    }

  onMounted(async () => {
  $('#phone').mask('(00) 00000-0000')

          if (accessToken.value) {
          const payload = await decodeJwtPayload(accessToken.value);
          if (payload && payload.sub) userId.value = payload.sub;
        }else{
          router.push('/sign-in')
        }
    await userdata(); 

      })
      
</script>

<style>
.nav-pills .nav-link.active {
  background-color: #2CA7B8;  /* Cor de fundo para o link ativo */
  color: white;               /* Cor do texto no ativo */
}

.nav-pills .nav-link {
  color: #2CA7B8;             /* Cor dos links inativos */
}

.nav-pills .nav-link:hover {
  color: #00C896;
}
</style>