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
                                        <router-link :to="`/controlpanel/`" class="nav-link" href="#"><i class="fas fa-user me-2"></i>Minha conta</router-link >
                                        <router-link :to="`/controlpanel/pedidos/`" class="nav-link " href="#"><i class="bi bi-clipboard me-2"></i>Pedidos</router-link >
                                        <router-link :to="`/controlpanel/cartoes/`" class="nav-link " href="#"><i class="fas fa-credit-card me-2"></i>Meus cartões</router-link >
                                        <router-link :to="`/controlpanel/atividade/`" class="nav-link active" href="#"><i class="fas fa-chart-line me-2"></i>Atividade</router-link >
                                        </div>
                                </div>
                            </div>

                            <!-- Content Area -->
                            <div class="col-lg-9">
                                <div class="p-4">
                                    <!-- Personal Information -->
                                    

                                 

                                    <!-- Recent Activity -->
                                    <div>
                                        <div>
                                        <h5 class="mb-4">Recent Activity</h5>
                                        <div class="activity-item mb-3">
                                            <h6 class="mb-1">Updated profile picture</h6>
                                            <p class="text-muted small mb-0">2 hours ago</p>
                                        </div>
                                        <div class="activity-item mb-3">
                                            <h6 class="mb-1">Changed password</h6>
                                            <p class="text-muted small mb-0">Yesterday</p>
                                        </div>
                                        <div class="activity-item">
                                            <h6 class="mb-1">Updated billing information</h6>
                                            <p class="text-muted small mb-0">3 days ago</p>
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
    </div>
</div>
</template>

<script setup>

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


.activity-item {
    border-left: 2px solid #e9ecef;
    padding-left: 20px;
    position: relative;
}

.activity-item::before {
    content: '';
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: #4158D0;
    position: absolute;
    left: -7px;
    top: 5px;
}
</style>