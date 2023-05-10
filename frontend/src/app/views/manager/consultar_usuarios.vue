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
                    <th>email</th>
                    <th>CPF</th>
                    <th>Tipo</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="user in filteredUsers">
                    <td>{{ user.name }}</td>
                    <td>{{ user.email }}</td>
                    <td>{{ user.document }}</td>
                    <td>{{ user.type }}</td>
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
export default {
  name: "ConsultarUsuarios",
  data() {
    return {
      selected: "" as any,
      options: [
        { id: 1, label: "Aluno" },
        { id: 2, label: "Professor" },
        { id: 3, label: "Fornecedor" },
      ],
      filter: {
        name: "",
        email: "",
        document: "",
        type: "",
      },
      users: [
        {
          name: "Nome",
          email: "email@email.com",
          document: "111.111.111-11",
          type: "Aluno",
        },
        {
          name: "Nome",
          email: "email@email.com",
          document: "111.111.111-11",
          type: "Aluno",
        },
        {
          name: "Nome",
          email: "email@email.com",
          document: "111.111.111-11",
          type: "Aluno",
        },
        {
          name: "Cavalo",
          email: "email@email.com",
          document: "111.111.111-11",
          type: "Aluno",
        },
        {
          name: "Nome",
          email: "email@email.com",
          document: "111.111.111-11",
          type: "Professor",
        },
        {
          name: "Nome",
          email: "email@email.com",
          document: "111.111.111-11",
          type: "Professor",
        },
        {
          name: "Nome",
          email: "email@email.com",
          document: "111.111.111-11",
          type: "Professor",
        },
        {
          name: "Nome",
          email: "email@email.com",
          document: "111.111.111-11",
          type: "Professor",
        },
        {
          name: "Nome",
          email: "email@email.com",
          document: "111.111.111-11",
          type: "Professor",
        },
        {
          name: "Nome",
          email: "email@email.com",
          document: "999.999.999-99",
          type: "Fornecedor",
        },
        {
          name: "Nome",
          email: "email@email.com",
          document: "111.111.111-11",
          type: "Fornecedor",
        },
        {
          name: "Nome",
          email: "cachorro@email.com",
          document: "111.111.111-11",
          type: "Fornecedor",
        },
      ],
    };
  },
  computed: {
    filteredUsers() {
      // this.filter.type = this.selected.label as string;
      return this.users.filter((user) => {
        return (
          user.name.includes(this.filter.name) &&
          user.email.includes(this.filter.email) &&
          user.document.includes(this.filter.document) &&
          user.type.includes(this.filter.type)
        );
      });
    },
  },
  watch: {
    selected: function(val, oldVal) {
      this.filter.type = val.label;
    },
  },
  methods: {
    log(value: any) {
      console.log(value);
    },
  },
};
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
