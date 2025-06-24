export async function autentication() {
    // console.log(token)   
    const token = localStorage.getItem('token');
    const response = await fetch('http://localhost:5000/rota-protegida', {
    method: 'GET',
    headers: {
        'Authorization': `Bearer ${token}`
    }
    });
    // console.log(response)
  
    // const data = await res.json();
    return response;
  }
  