import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    host: '0.0.0.0',  // Permite que qualquer dispositivo na rede acesse
    port: 3000,
    allowedHosts: [
      'afde-2804-29b8-5186-9989-86d-b2c3-1f1a-8a2.ngrok-free.app',  // URL gerada pelo ngrok
      // Você pode adicionar mais hosts aqui, se necessário
    ],// Você pode mudar a porta conforme necessário
  }
})
