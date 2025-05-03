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

document.addEventListener('DOMContentLoaded', function () {
  const sidebarLinks = document.querySelectorAll('.sidebar a');

  sidebarLinks.forEach(link => {
    const isAnchor = link.getAttribute('href').startsWith('#');
    const currentPath = window.location.pathname;

    if (!isAnchor && link.pathname === currentPath) {
      link.classList.add('active');
    }

    link.addEventListener('click', function () {
      sidebarLinks.forEach(l => l.classList.remove('active'));
      this.classList.add('active');
    });
  });

  const logoutLink = document.getElementById("logout-link");

  if (logoutLink) {
    logoutLink.addEventListener("click", function (event) {
      event.preventDefault();
      const confirmLogout = confirm("Você realmente deseja sair?");
      if (confirmLogout) {
        window.location.href = logoutLink.dataset.logoutUrl;
      }
    });
  }

  if (typeof lucide !== 'undefined') {
    lucide.createIcons();
  }
});
