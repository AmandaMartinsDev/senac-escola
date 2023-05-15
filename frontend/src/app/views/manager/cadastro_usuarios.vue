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
                v-model="userType"
                :options="options"
                autocomplete
                placeholder="Escolha o tipo do usuário"
              />
            </i-column>
            <i-column sm="5" md="12">
              <i-form><h2>Nome:</h2></i-form>
              <i-input v-model="user.user_name" placeholder="Digite aqui..." />
            </i-column>
            <i-column sm="5" md="12">
              <i-form><h2>CPF:</h2></i-form>
              <i-input v-model="user.document_id"  placeholder="Digite aqui..." maxlength="11" />
            </i-column>
            <i-column sm="5" md="12">
              <i-form><h2>Email:</h2></i-form>
              <i-input
                v-model="user.user_email"
                placeholder="Digite aqui..."
                type="email"
              />
            </i-column>
            <i-column sm="5" md="12">
              <i-form><h2>Senha Provisória:</h2></i-form>
              <i-input
                v-model="user.user_password"
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
      <i-button class="_margin-left:1 e-button" color="primary" @click="create"
        >Concluir</i-button
      >
    </div>
  </i-layout-content>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { UserCreate } from '../../model/user.model';
import { UserType } from '../../model/user-type.enum';
import { createUser } from '../../services/users-service';

export default defineComponent({
  name: "CadastroUsuarios",
  setup() {
    const user = ref(<UserCreate>{});
    const userType = ref(<{ id: string, label: string}>{})
    const options = ref([
      { id: "STUDENT", label: "Aluno" },
      { id: "TEACHER", label: "Professor" },
      { id: "SUPPLIER", label: "Fornecedor" },
      { id: "MANAGER", label: "Gerente" },
    ]);

    const create = () => {
      user.value.user_type = userType.value.id as UserType
      user.value.user_address = "Ruas dos bobos, nº " + Math.floor(Math.random() * 1000) + " - Bairro dos bobos"
      user.value.user_phone = parseInt("119" + Math.floor(Math.random() * 100000000))
      console.log("user ", user.value)
      createUser(user.value).then(response => {
        console.log("response ", response)
      }, error => {
        console.log("error ", error)
      })
    }
    return {
      user,
      userType,
      options,
      create
    };
  },
});
</script>

<style lang="scss">
.botoes {
  display: flex;
  justify-content: flex-end;
  width: 100%;
}
</style>
