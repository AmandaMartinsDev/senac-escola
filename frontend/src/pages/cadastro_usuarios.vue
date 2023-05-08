<template>
    <i-layout vertical>
      <i-layout-content
        class="_display:flex _align-items:center _justify-content:center"
        ><img src="/src/assets/logo-light-mode.webp" alt=""
      /></i-layout-content>
      <i-layout-content
        class="_display:flex _align-items:center _justify-content:center"
        style="min-height: 100vh; background-color: var(--color--gray-10)"
        ><i-form style="min-width: 1324px">
          <i-container style="min-height: 95vh; min-width: 1000px">
                <i-row>
                  <i-form class='_margin-left:4' ><h2>Cadastro de Usuários</h2></i-form>
                </i-row>
              <i-container style="max-width: 1200px;">
                <i-row style="max-width: 500px;">
                  <i-column sm="2" md="12" >
                      <i-form><h2>Tipo:</h2></i-form>
                        <i-select 
                            v-model="selected"
                            :options="options"
                            autocomplete
                            placeholder="Escolha o tipo do usuário"
                            @search="onSearch"
                        />
                    </i-column>
                    <i-column sm="5" md="12" >
                      <i-form ><h2>Nome:</h2></i-form>
                      <i-input v-model="value" placeholder="Digite aqui..." />
                    </i-column>
                    <i-column sm="5" md="12">
                      <i-form><h2>CPF:</h2></i-form>
                      <i-input v-model="value" placeholder="Digite aqui..." />
                    </i-column>
                    <i-column sm="5" md="12" >
                      <i-form><h2>Email:</h2></i-form>
                      <i-input v-model="value" placeholder="Digite aqui..." type="email"/>
                    </i-column>
                    <i-column sm="5" md="12" >
                      <i-form><h2>Senha Provisória:</h2></i-form>
                      <i-input v-model="value" placeholder="Digite aqui..." type="password"/>
                    </i-column>
                </i-row>
            </i-container>
        </i-container>
        <div class="botoes">
        <i-button  color="danger">Cancelar</i-button>
        <i-button  class='_margin-left:1' color="primary">Consultar</i-button>
      </div>
      </i-form> </i-layout-content>
    </i-layout>
  </template>

<script>
    export default{
        name:'Home'
    }
</script>