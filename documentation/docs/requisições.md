# Requisições 📃

Para fazer requisições no backend da aplicação, você deve seguir os seguintes passos:

- Executar o backend da aplicação, conforme indicado na documentação de [configurações](configurações).

- Realizar requisições pelos seguintes métodos:
- - Acessar o endereço informado no terminal, ou adicionar o final `/docs` ao endereço para acessar a documentação da API.
- - Utilizar o [Insomnia](https://insomnia.rest/download/) ou [Postman](https://www.postman.com/downloads/) para fazer requisições.
- - Utilizar o curl, como por exemplo, com o comando abaixo:

<!-- termynal -->

```console
$ curl --request GET \
  --url http://127.0.0.1:5010/
{"Hello":"World"}
```

> ⚠️ Para requisições pelo Insomnia, você pode importar o arquivo disponibilizado na pasta `insomnia`.
