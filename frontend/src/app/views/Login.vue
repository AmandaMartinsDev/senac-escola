<template>
  <i-layout vertical>
    <i-layout-content
      class="_display:flex _align-items:center _justify-content:center"
      ><img src="/src/assets/logo-light-mode.webp" alt=""
    /></i-layout-content>
    <i-layout-content
      class="_display:flex _align-items:center _justify-content:center"
      style="min-height: 100vh; background-color: var(--color--gray-10)"
      ><i-form style="min-width: 360px">
        <i-form><h2>Acesse sua conta</h2></i-form>
        <i-form-group>
          <i-form-label>Email:</i-form-label>
          <i-input name="email" placeholder="Digite o seu email aqui..." />
        </i-form-group>
        <i-form-group>
          <i-form-label>Senha:</i-form-label>
          <i-input
            name="password"
            type="password"
            placeholder="Digite a sua senha aqui..."
          />
        </i-form-group>
        <i-form-group style="text-align: center">
          <i-button color="primary" class="purple-button" type="submit">
            Acessar
          </i-button>
        </i-form-group>
        <i-form-group style="text-align: center">
          <i-button link color="dark">Esqueci minha senha</i-button>
        </i-form-group>
      </i-form></i-layout-content
    >
  </i-layout>
</template>

<style scoped lang="scss">
h2 {
  text-align: center;
}

.purple-button {
  display: flex;
  background-color: #3d50ff;
  font-weight: bold;
  font-size: 16px;
  color: #ffffff !important;
  padding: 0 30px;
  height: 55px;
  border-radius: 50px !important;
  margin: 0 auto;
}
</style>
