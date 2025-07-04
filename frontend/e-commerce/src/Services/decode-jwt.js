export async function decodeJwtPayload(token) {
    try {
    //   console.log(token)
      const base64Url = token.split('.')[1];
      const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
      const jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
      }).join(''));
  
    //   console.log(jsonPayload)
      return JSON.parse(jsonPayload);
    } catch (error) {
      console.error('Erro ao decodificar o JWT:', error);
      return null;
    }
  }