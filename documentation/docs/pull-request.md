# Enviando a pull request 📦

Para enviar a sua pull request, basta seguir os passos abaixo:

- Verificar as alterações feitas no código com o comando abaixo:

<!-- termynal -->

```console
$ git status
```

- Adicionar as alterações feitas no código com o comando abaixo:

<!-- termynal -->

```console
$ git add .
ou
$ git add <nome_do_arquivo_ou_pasta>
```

- Criar um commit com as alterações feitas no código com o comando abaixo:

<!-- termynal -->

```console
$ git commit -m "Mensagem do commit"
```

- Enviar as alterações feitas no código para o repositório remoto com o comando abaixo:

<!-- termynal -->

```console
$ git push
---> 100%
```

> ⚠️ Antes de enviar a pull request, execute as ferramentas de qualidade de código, com os comandos abaixo:

## 🛠️ Backend

- Abrir a pasta `backend` ou rodar o comando abaixo:

<!-- termynal -->

```console
$ cd backend
```

- Executar as ferramentas de qualidade de código com o comando abaixo:

<!-- termynal -->

```console
$ poetry run task lint
---> 100%
```

## 🎨 Frontend

- Abrir a pasta `frontend` ou rodar o comando abaixo:

<!-- termynal -->

```console
$ cd frontend
```

- Executar as ferramentas de qualidade de código com o comando abaixo:

<!-- termynal -->

```console
$ npm run lint
---> 100%
```
