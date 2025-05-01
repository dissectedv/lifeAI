function showForm(type) {
    const login = document.getElementById('loginForm');
    const register = document.getElementById('registerForm');
    const btnLogin = document.getElementById('btn-login');
    const btnRegister = document.getElementById('btn-register');
  
    if (type === 'login') {
      login.classList.remove('hidden');
      register.classList.add('hidden');
      btnLogin.classList.add('active');
      btnRegister.classList.remove('active');
    } else {
      login.classList.add('hidden');
      register.classList.remove('hidden');
      btnLogin.classList.remove('active');
      btnRegister.classList.add('active');
    }
  }
  
  window.onload = function () {
    showForm('register'); 
  };
  