<template>
  <i-layout class="nav-bar">
    <i-layout-header class="nav-header">
      <img class="logo" src="src/assets/logo-light-mode.webp" alt="" />
    </i-layout-header>

    <i-layout-content
      class="_height:100% _display:flex _flex-direction:column _justify-content:space-between"
    >
      <i-layout>
        <i-layout-header
          class="_display:flex _flex-direction:column _justify-content:space-between user"
        >
          <img
            class="userThumb _border-radius:circle"
            src="https://s.dicionariofinanceiro.com/imagens/elon-musk-0.jpg"
            alt=""
          />
          <span class="cargo">Gerente Escolar</span>
          <h1 class="greeting">Olá Elon,</h1>
        </i-layout-header>

        <i-layout-content class="nav-content">
          <i-button to="/consulta-usuario"
            class="action-button"
          >
            <span>Consultar usuários</span>
            <img src="src/assets/users-icon.svg" alt="" />
          </i-button>
          <i-button to="/cadastro-usuario"
            class="action-button"
          >
            <span>Cadastros de usuários</span>
          </i-button>
          <i-button to="/altera-usuario"
            class="action-button"
          >
            <span>Alterar usuários</span>
          </i-button>
          <i-button to="/excluir-usuario"
            class="action-button"
          >
            <span>Excluir usuários</span>
          </i-button>
        </i-layout-content>
      </i-layout>
    </i-layout-content>

    <i-layout-footer class="_display:flex _justify-content:start nav-footer">
        <i-button to="/login"
          color="danger"
          class="_border-radius _display:flex _justify-content:space-between logout-button"
        >
          <span>Sair</span>
          <img src="src/assets/logout-icon.png" alt="" />
        </i-button>
      <i-button to="/minha-conta" color="light" class="_border-radius:circle account-config">
        <img src="src/assets/account-config-icon.svg" alt="" />
      </i-button>
    </i-layout-footer>
  </i-layout>
</template>

<script lang="ts">

export default {
  components: {
  },
};
</script>

<style scoped lang="scss">
@import "https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;700&display=swap";
.nav-bar {
  padding: 40px;
  padding-right: 70px;
  width: 400px;
  height: 100vh;
  font-family: "Noto Sans", sans-serif;

  .nav-header {
    .logo {
      width: 114px;
    }
  }
  .user {
    .userThumb {
      width: 100px;
      margin-top: 65px;
    }

    .cargo {
      margin-top: 30px;
      font-size: 16px;
      font-weight: bold;
      color: #6b6b6b;
    }

    .greeting {
      margin-top: 8px;
      font-size: 24px;
      font-weight: bold;
    }
  }

  .nav-content {
    display: flex;
    flex-direction: column;
    gap: 15px;
    .action-button {
      display: flex;
      justify-content: space-between;
      background-color: #6b7aff;
      font-weight: bold;
      font-size: 16px;
      color: #ffffff;
      width: 100%;
      height: 55px;
      border-radius: 50px !important;
      padding-left: 28px;
      padding-right: 31px;
      &:hover {
        background-color: #3d50ff;
        color: #ffffff;
      }
      &:focus {
        background-color: #3d50ff;
        color: #ffffff;
      }
    }
  }

  .nav-footer {
    gap: 20px;
    .logout-button {
      width: 120px;
      height: 55px;
      border-radius: 50px !important;
      padding-left: 28px;
      padding-right: 24px;
      font-weight: bold;
    }

    .account-config {
      width: 55px;
      height: 55px;
      background-color: #fff;
      box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.15), inset 0px 1px 1px rgba(0, 0, 0, 0.15);
      border: none;
      border: 1px 1px 0 0 solid #e5e5e5;
      &:hover {
        background-color: #e5e5e5;
      }
    }
  }
}
</style>
