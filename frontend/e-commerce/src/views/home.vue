<script setup>
import destaques from '../components/destaques.vue'
import cards from '../components/cards.vue';
import colecoes  from '../components/colecoes.vue';
</script>

<template>
      <destaques></destaques>
      <cards :text="'Mais vendidos'":card=1></cards>
      <colecoes></colecoes>
      <cards :text="'Em promoção'" :card=2></cards>
      <cards :text="'Explore novas ideias'"></cards>

</template>
