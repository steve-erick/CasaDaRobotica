<template>
  <div class="container flex items-center justify-around h-screen">
    <div class="card shadow p-4" style="max-width: 400px; width: 100%;">
      <h2 class="text-center mb-4">Login</h2>
      <form @submit.prevent="loginform">
        <div class="mb-3">
          <label for="email" class="form-label">E-mail</label>
          <input
            v-model="form.email"
            type="email"
            class="form-control"
            id="email"
            placeholder="seu@email.com"
            required
          />
        </div>
        <div class="mb-3">
          <label for="senha" class="form-label">Senha</label>
          <input
            v-model="form.password"
            type="password"
            class="form-control"
            id="senha"
            placeholder="Digite sua senha"
            required
          />
        </div>
        <div class="d-grid">
          <button type="submit" class="text-center btn" style="background: #00FF9C;">Entrar</button>
        </div>
        <p v-if="mensagem" class="mt-3 text-center text-danger">{{ mensagem }}</p>
      </form>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref, onMounted } from 'vue'
import axios from 'axios'
import { autentication } from '../Services/autentication' // ajuste esse caminho conforme seu projeto
import { useRouter } from 'vue-router'

// estado reativo do formulário
const form = reactive({
  email: '',
  password: '',
})

// mensagem para feedback
const mensagem = ref('')

// acesso ao roteador
const router = useRouter()

// chamada ao login
const loginform = async () => {
  try {
    const response = await axios.post('http://127.0.0.1:5000/users/login', {
      login: [
        {
          email: form.email,
          password: form.password,
        }
      ]
    });

    const token = response.data.access_token
    localStorage.setItem('token', token)
    window.location.replace('/');

    // router.push('/dashboard') // redireciona após login
  } catch (error) {
    mensagem.value = "Email ou senha incorretos!"
    console.error('Erro:', error);
  }
}

// verifica token assim que o componente é montado
onMounted(async () => {
  try {
    const res = await autentication();

    console.log(res)
    if (res.status == 200) {
      const data = await res.json();
      // router.push('/');
    } else if (res.status === 401) {
      mensagem.value = "Token inválido. Redirecionando para login...";
      localStorage.removeItem('Token');
      // router.push('/login');
    }
  } catch (err) {
    console.error("Erro na verificação de autenticação:", err);
  }
});
</script>
