<script setup>
import navbar from './components/navbar.vue'
import footbar from './components/footbar.vue';
import { RouterView } from 'vue-router';
</script>

<template>
  <div class="d-flex flex-col min-h-screen bg-light">
    <navbar />
    <div class="flex-grow">
      <router-view :key="$route.params.id" />
    </div>
    <footbar />
  </div>
</template>

<style>
#app{
 margin: 0;
 background-color: #eee;
}
</style>