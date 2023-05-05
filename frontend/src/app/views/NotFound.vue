<template>
  <i-layout vertical>
    <i-layout-content
      class="_display:flex _align-items:center _justify-content:center _flex-direction:column"
    >
      <img src="/src/assets/logo-light-mode.webp" alt="" />
      <h1>Página não encontrada</h1>
      <i-button :to="{ name: 'Login' }" class="purple-button">
        Voltar
      </i-button>
    </i-layout-content>
  </i-layout>
</template>

<style scoped lang="scss">
.purple-button {
  display: flex;
  justify-content: space-between;
  background-color: #6b7aff;
  font-weight: bold;
  font-size: 16px;
  color: #ffffff !important;
  height: 55px;
  border-radius: 50px !important;
  padding-left: 28px;
  padding-right: 31px;
  &:hover {
    background-color: #3d50ff;
  }
  &:focus {
    background-color: #3d50ff;
  }
}
</style>
