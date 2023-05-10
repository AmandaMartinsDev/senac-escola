<template>
  <i-layout-content
    class="_display:flex _align-items:center _justify-content:space-between _flex-direction:column e-content"
  >
    <i-container>
      <i-layout-header class="e-header">
        <h2>Cadastro de Usuários</h2>
      </i-layout-header>
      <i-form>
        <i-container>
          <i-row class="_width:50%">
            <i-column sm="2" md="12">
              <i-form><h2>Tipo:</h2></i-form>
              <i-select
                v-model="selected"
                :options="options"
                autocomplete
                placeholder="Escolha o tipo do usuário"
                @search="onSearch"
              />
            </i-column>
            <i-column sm="5" md="12">
              <i-form><h2>Nome:</h2></i-form>
              <i-input v-model="value" placeholder="Digite aqui..." />
            </i-column>
            <i-column sm="5" md="12">
              <i-form><h2>CPF:</h2></i-form>
              <i-input v-model="value" placeholder="Digite aqui..." />
            </i-column>
            <i-column sm="5" md="12">
              <i-form><h2>Email:</h2></i-form>
              <i-input
                v-model="value"
                placeholder="Digite aqui..."
                type="email"
              />
            </i-column>
            <i-column sm="5" md="12">
              <i-form><h2>Senha Provisória:</h2></i-form>
              <i-input
                v-model="value"
                placeholder="Digite aqui..."
                type="password"
              />
            </i-column>
          </i-row>
        </i-container>
      </i-form>
    </i-container>
    <div class="botoes">
      <i-button class="e-button e-danger">Cancelar</i-button>
      <i-button class="_margin-left:1 e-button" color="primary"
        >Concluir</i-button
      >
    </div>
  </i-layout-content>
</template>

<script>
export default {
  name: "CadastroUsuarios",
  data() {
    return {
      selected: null,
      options: [
        { id: 1, label: "Aluno - Pessoa Física" },
        { id: 2, label: "Professor - Pessoa Física" },
        { id: 3, label: "Professor - Pesso Jurídica" },
        { id: 4, label: "Fornecedor - Pesso Jurídica" },
      ],
    };
  },
};
</script>

<style lang="scss">
.botoes {
  display: flex;
  justify-content: flex-end;
  width: 100%;
}
</style>
