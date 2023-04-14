# Configuração 🛠️

Para utilizar o projeto, é necessário seguir os passos abaixo para cada parte da aplicação, começando por:

- Clonar o repositório:

<!-- termynal -->

```console
$ git clone https://github.com/AmandaMartinsDev/senac-escola.git
---> 100%
```

- Abrir a pasta onde foi clonado o repositório.

---

## 🗃️ Banco de Dados

- Abrir a pasta `database` ou rodar o comando abaixo:

<!-- termynal -->

```console
$ cd database
```

- Rodar o comando abaixo para subir o container do banco de dados (Postgresql) e do administrador de banco de dados (PgAdmin4):

<!-- termynal -->

```console
$ docker-compose up -d
---> 100%
```

- Verificar o endereço do PgAdmin4 no terminal com o comando abaixo:

<!-- termynal -->

```console
$ docker inspect pgadmin | grep "IPAddress"
                           "SecondaryIPAddresses": null,
                           "IPAddress": "",
                                   "IPAddress": "172.18.0.2",
```

- Acessar o PgAdmin4 no endereço informado na última linha (nesse exemplo, seria o `http://172.18.0.2`), com as credenciais abaixo:

> Email: admin@admin.com
> Senha: 123

- Criar uma nova conexão com o banco de dados, utilizando as informações abaixo:

> Name: Escola
> Host name/address: postgres
> Port: 5432
> Maintenance database: escola
> Username: admin
> Password: 123

> 💡 Ative a opção "Save password?" para não precisar digitar a senha toda vez que for acessar o banco de dados.

- Verificar se as tabelas e dados foram criados no banco de dados.

- Localizar o endereço do banco de dados no terminal com o comando abaixo (irá ser utilizado para configurar o connection string do backend):

<!-- termynal -->

```console
$ docker inspect postgres | grep "IPAddress"
                            "SecondaryIPAddresses": null,
                            "IPAddress": "",
                                    "IPAddress": "172.18.0.3",
```

> 💡 Caso queira parar a execução do container, basta rodar o comando: `docker-compose down`.

> ⚠️ Ao parar a execução do container, todos os dados serão perdidos.

---

## 🛠️ Backend

- Abrir a pasta `backend` ou rodar o comando abaixo:

<!-- termynal -->

```console
$ cd backend
```

- Criar o arquivo `.env` na raíz do projeto.

- Editar o arquivo `.env` conforme o exemplo abaixo, ajustando o seu endereço local do banco de dados na connection string.

```env
DATABASE_URL=postgresql://admin:123@172.19.0.2/escola
```

- Instalar as dependências com o comando abaixo:

<!-- termynal -->

```console
$ poetry install
---> 100%
```

- Rodar o ambiente de desenvolvimento com o comando abaixo:

<!-- termynal -->

```console
$ poetry run task dev
INFO:     Will watch for changes in these directories: ['/home/amanda/Documents/Projects/senac-escola/backend']
INFO:     Uvicorn running on http://127.0.0.1:5010 (Press CTRL+C to quit)
INFO:     Started reloader process [27955] using WatchFiles
INFO:     Started server process [27960]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

- Fazer as [requisições](requisições) autenticadas no endereço informado na segunda linha de informações (nesse exemplo, seria o `http://127.0.0.1:5010`).

> 💡 Você pode parar o ambiente de desenvolvimento fechando o terminal ou pressionando CTRL + C.

> ⚠️ O comando `poetry run task prod` é destinado para rodar a aplicação em produção na [Render](render.com/).

---

## 🎨 Frontend´

- Abrir a pasta `frontend` ou rodar o comando abaixo:

<!-- termynal -->

```console
$ cd frontend
```

- Instalar as dependências com o comando abaixo:

<!-- termynal -->

```console
$ npm install
---> 100%
```

- Rodar o ambiente de desenvolvimento com o comando abaixo:

<!-- termynal -->

```console
$ npm run dev

> escola_frontend@0.1.0 dev
> vite


  VITE v4.2.1  ready in 298 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h to show help
```

- Acessar o frontend pelo endereço informado na antepenúltima linha (nesse exemplo, seria o `http://localhost:5173/`).

> 💡 Você pode parar ambiente de desenvolvimento fechando o terminal ou pressionando CTRL + C.

---

## 📚 Documentação

- Abrir a pasta `documentation` ou rodar o comando abaixo:

<!-- termynal -->

```console
$ cd documentation
```

- Instalar as dependências com o comando abaixo:

<!-- termynal -->

```console
$ poetry install
---> 100%
```

- Rodar o ambiente de pré-visualização com o comando abaixo:

<!-- termynal -->

```console
$ poetry run mkdocs serve
INFO     -  Building documentation...
INFO     -  Cleaning site directory
INFO     -  Documentation built in 0.15 seconds
INFO     -  [19:48:03] Watching paths for changes: 'docs', 'mkdocs.yml'
INFO     -  [19:48:03] Serving on http://127.0.0.1:8000/senac-escola/
```

- Acessar a pré-visualização da documentação pelo endereço informado na última linha (nesse exemplo, seria o `http://127.0.0.1:8000/senac-escola/`).

> 💡 Você pode parar a pré-visualização fechando o terminal ou pressionando CTRL + C.
