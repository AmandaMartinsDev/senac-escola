<template>
  <i-layout vertical>
    <i-layout-content
      class="_margin-top:8 _padding-top:8 _display:flex _align-items:center _justify-content:center _flex-direction:column"
    >
      <img src="/src/assets/logo-light-mode.webp" alt="" />
      <h1>Página não encontrada</h1>
      <router-link :to="{ name: 'Login' }">
        <i-button outline color="primary"> Voltar </i-button>
      </router-link>
    </i-layout-content>
  </i-layout>
</template>
