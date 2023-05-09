const routes = [
  {
    path: "/login",
    name: "Login",
    component: () => import("../views/Login.vue"),
  },
  /* Adicione rotas */
  {
    path: "/consultar-usuarios",
    name: "ConsultarUsuarios",
    component: () => import("../views/manager/consultar_usuarios.vue")
  },
  {
    path: "/cadastro-usuarios",
    name: "CadastroUsuarios",
    component: () => import("../views/manager/cadastro_usuarios.vue")
  },
  {
    path: "/alterar-usuarios",
    name: "AlterarUsuarios",
    component: () => import("../views/manager/alterar_usuarios.vue")
  },
  {
    path: "/excluir-usuarios",
    name: "ExcluirUsuarios",
    component: () => import("../views/manager/excluir_usuarios.vue")
  },
  {
    path: "/:pathMatch(.*)*",
    name: "NotFound",
    component: () => import("../views/NotFound.vue"),
  }
];

export default routes;
