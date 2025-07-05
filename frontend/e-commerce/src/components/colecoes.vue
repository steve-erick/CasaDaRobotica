<template>
    <div class="d-flex justify-center p-4 mt-24">
        <div class="pr-8">
            <router-link :to="`/search/embarcados`" class="no-underline text-black">
                <img :src="getImageUrl('categorie1.webp')" loading="lazy" alt="" class="colection-img" style="width: 200px; height: 200px;">  
                <p class="text-center decoration-0">Embarcados</p>  
            </router-link>
        </div>

        <div class="pr-8">
         <router-link :to="`/search/Sensor  `" class="no-underline text-black" >
            <img :src="getImageUrl('categorie2.webp')" loading="lazy" alt="" class="colection-img" style="width: 200px; height: 200px;"> 
            <p class="text-center">Sensores e atuadores</p>  
        </router-link>

        </div>

        <div class="pr-8">
            <router-link :to="`/search/Robotica`" class="no-underline text-black">

            <img :src="getImageUrl('categorie3.webp')" loading="lazy" alt=""  class="colection-img" style="width: 220px; height: 200px;">
            <p class="text-center">Robotica</p>  
                        </router-link>

        </div>
        
        <div class="pr-8">
           <router-link :to="`/search/3d`" class="no-underline text-black">
            <img :src="getImageUrl('categories4.webp')" loading="lazy" alt="" class="colection-img" style="width: 200px; height: 200px;">
            <p class="text-center">Impressão 3d</p>  
                        </router-link>

        </div>

        


        </div>
</template>

<script setup>
import { computed } from 'vue';
    import { useRouter } from 'vue-router' // <== Adicione isso

const baseUrl = "http://127.0.0.1:5000/images/";

const getImageUrl = (filename) => {
    return `${baseUrl}${filename}`;
};
  </script>

  <style>
    .colection-img:hover{
        transform: scale(1.1);
        transition: 0.3s ease-in-out;
        padding-bottom: 10px;
    }
</style>
  