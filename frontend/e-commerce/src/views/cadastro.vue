

<template>
  <div class="container flex items-center justify-around mt-10">
    <div class="card shadow p-4" style="max-width: 500px; width: 100%;">
      <h2 class="text-center mb-4">Cadastro</h2>
      <form @submit.prevent="submitForm">
        <div class="mb-3">
          <label for="nome" class="form-label">Nome Completo</label>
          <input v-model="form.name" type="text" class="form-control" id="nome" placeholder="Seu nome" required>
        </div>
        <div class="mb-3">
          <label for="Telefone" class="form-label">Telefone</label>
          <input v-model="form.phone" type="text" class="form-control" id="Telefone" placeholder="Seu Telefone" required>
        </div>
        <div class="mb-3">
          <label for="Addres" class="form-label">Endereço</label>
          <input v-model="form.address" type="text" class="form-control" id="Addres" placeholder="Seu Endereço" required>
        </div>
        <div class="mb-3">
          <label for="email" class="form-label">E-mail</label>
          <input v-model="form.email" type="email" class="form-control" id="email" placeholder="seu@email.com" required>
        </div>
        <div class="mb-3">
          <label for="senha" class="form-label">Senha</label>
          <input v-model="form.password" type="password" class="form-control" id="senha" placeholder="Crie uma senha" required>
        </div>
        <div class="mb-3">
          <label for="confirmarSenha" class="form-label">Confirmar Senha</label>
          <input v-model="form.confirmPassword" type="password" class="form-control" id="confirmarSenha" placeholder="Confirme a senha" required>
        </div>
        <div class="d-grid">
          <button type="submit" class="text-center btn" style="background: #00FF9C;">Cadastrar</button>
        </div>
      </form>
      <div class="text-center mt-3">
        <small>Já tem uma conta? <a href="#">Faça login</a></small>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive,onMounted} from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { autentication } from '../Services/autentication' // ajuste esse caminho conforme seu projeto
const router = useRouter()


onMounted(async () => {
  try {
    const res = await autentication();
    console.log(res)
    if (res.ok) {
      // const data = await res.json();
      router.push('/');
    } else if (res.status === 401) {
      mensagem.value = "Token inválido. Redirecionando para login...";
      localStorage.removeItem('token');
      router.push('/login');
    }
  } catch (err) {
    console.error("Erro na verificação de autenticação:", err);
  }
});
const form = reactive({
  name: '',
  phone: '',
  email: '',
  password: '',
  confirmPassword: '',
  address: ''
})

const submitForm = async () => {
  if (form.password !== form.confirmPassword) {
    alert('As senhas não coincidem!');
    return;
  }

  try {
    const response = await axios.post('http://127.0.0.1:5000/users/cadastro', {
      newUser: [
        {
          name: form.name,
          phone: form.phone,
          email: form.email,
          password: form.password,
          address: form.address
        }
      ]
    });
    // console.log('Resposta:', response.data);
    localStorage.setItem('token', response.data.access_token);
    router.push('/');
  } catch (error) {
    console.error('Erro:', error);
  }
}
</script>