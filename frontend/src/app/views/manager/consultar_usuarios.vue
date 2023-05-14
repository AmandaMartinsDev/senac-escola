<template>
  <i-layout-content
    class="_display:flex _align-items:center _justify-content:space-between _flex-direction:column e-content"
  >
    <i-container>
      <i-layout-header class="e-header">
        <h2>Consultar Usuários</h2>
      </i-layout-header>
      <i-form>
        <i-container>
          <i-row>
            <i-column sm="5" md="6">
              <i-form><h2>Tipo:</h2></i-form>
              <i-select
                v-model="selected"
                :options="options"
                autocomplete
                placeholder="Escolha o tipo do usuário"
                clearable
              />
            </i-column>
            <i-column sm="5" offset-sm="2" md="6" offset-md="0">
              <i-form><h2>Nome:</h2></i-form>
              <i-input v-model="filter.name" placeholder="Digite aqui..." />
            </i-column>
            <i-column sm="5" md="6">
              <i-form><h2>CPF:</h2></i-form>
              <i-input v-model="filter.document" placeholder="Digite aqui..." />
            </i-column>
            <i-column sm="5" offset-sm="2" md="6" offset-md="0">
              <i-form><h2>Email:</h2></i-form>
              <i-input
                v-model="filter.email"
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
              <i-table v-if="filteredUsers.length > 0" class="e-table">
                <thead>
                  <tr>
                    <th>Nome</th>
                    <th>Email</th>
                    <th>CPF</th>
                    <th>Tipo</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="user in filteredUsers">
                    <td>{{ user.user_name }}</td>
                    <td>{{ user.user_email }}</td>
                    <td>{{ user.document_id }}</td>
                    <td>{{ user.user_type }}</td>
                  </tr>
                </tbody>
              </i-table>
            </i-column>
          </i-row>
        </i-container>
      </i-form>
    </i-container>
    <div class="botoes">
      <i-button class="e-button e-danger">Cancelar</i-button>
      <i-button class="_margin-left:1 e-button">Consultar</i-button>
    </div>
  </i-layout-content>
</template>

<script lang="ts">
import { User } from "../../model/user.model";
import { UserType } from "../../model/user-type.enum";
import { defineComponent, ref, computed, onMounted } from "vue";
import { listUsers } from "../../services/users-service";
import { maskCpf } from '../../util/mask-cpf';

export default defineComponent({
  name: "ConsultarUsuarios",
  setup() {
    const selected = ref();
    const options = ref([
      { id: "STUDENT", label: "Aluno" },
      { id: "TEACHER", label: "Professor" },
      { id: "FORNECEDOR", label: "Fornecedor" },
      { id: "MANAGER", label: "Gerente" },
    ]);
    const filter = ref({
      name: "",
      email: "",
      document: "",
      type: "",
    });
    const users = ref([] as User[]);

    const filteredUsers = computed(() => {
      return users.value.filter((user) => {
        console.log("Filter: ", )
        return (
          user.user_name.includes(filter.value.name) &&
          user.user_email.includes(filter.value.email) &&
          user.document_id.toString().includes(filter.value.document) &&
          (selected.value == undefined || user.user_type == (<any>UserType)[selected.value.id])
        );
      });
    });

    const getUsers = () => {
      listUsers().then((response) => {
        console.log(response)
        users.value = response.data.map(user => {
          return {
            user_name: user.user_name,
            user_type: (<any>UserType)[user.user_type.toUpperCase()],
            document_id: maskCpf(user.document_id.toString()),
            user_address: user.user_address,
            user_phone: user.user_phone,
            user_email: user.user_email,
          }
        })
        console.log(users.value)
      });
    };

    onMounted(() => {
      getUsers();
    });

    return {
      selected,
      options,
      filter,
      users,
      filteredUsers,
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
.content {
  padding: 40px;
}
</style>
