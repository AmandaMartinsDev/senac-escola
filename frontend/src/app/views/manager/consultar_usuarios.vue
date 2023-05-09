<template>
  <i-layout vertical>
    <i-layout-content
      class="_display:flex _align-items:center _justify-content:center"
      style="min-height: 100vh; background-color: var(--color--gray-10)"
      ><i-form style="min-width: 1324px">
        <i-container style="min-height: 90vh; min-width: 1000px">
          <i-row class="_margin-bottom:1 _margin-left:3">
            <i-form><h2>Consultar Usuários</h2></i-form>
          </i-row>
          <i-container style="min-height: 40vh; max-width: 1100px">
            <i-row>
              <i-column sm="5" md="6">
                <i-form><h2>Tipo:</h2></i-form>
                <i-select
                  v-model="selected"
                  :options="options"
                  autocomplete
                  placeholder="Escolha o tipo do usuário"
                  @search="onSearch"
                />
              </i-column>
              <i-column sm="5" offset-sm="2" md="6" offset-md="0">
                <i-form><h2>Nome:</h2></i-form>
                <i-input v-model="value" placeholder="Digite aqui..." />
              </i-column>
              <i-column sm="5" md="6">
                <i-form><h2>CPF:</h2></i-form>
                <i-input v-model="value" placeholder="Digite aqui..." />
              </i-column>
              <i-column sm="5" offset-sm="2" md="6" offset-md="0">
                <i-form><h2>Email:</h2></i-form>
                <i-input
                  v-model="value"
                  placeholder="Digite aqui..."
                  type="email"
                />
              </i-column>
              <i-column
                sm="5"
                offset-sm="2"
                md="12"
                offset-md="0"
                class="_margin-top:4"
              >
                <i-table>
                  <thead>
                    <tr>
                      <th>Nome</th>
                      <th>email</th>
                      <th>CPF</th>
                      <th>Tipo</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>Nome</td>
                      <td>email@email.com</td>
                      <td>111.111.111-11</td>
                      <td>Pessoa Física</td>
                    </tr>
                  </tbody>
                </i-table>
              </i-column>
            </i-row>
          </i-container>
        </i-container>
        <div class="botoes">
          <i-button class="e-button e-danger">Cancelar</i-button>
          <i-button class="_margin-left:1 e-button">Consultar</i-button>
        </div>
      </i-form>
    </i-layout-content>
  </i-layout>
</template>

<script>
export default {
  name: "ConsultarUsuarios",
};
</script>

<style lang="scss">
.botoes {
  display: flex;
  justify-content: flex-end;
}
</style>