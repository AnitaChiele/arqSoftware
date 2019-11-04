> Written with [StackEdit](https://stackedit.io/).

# Instalando o projeto
Fazer up do container:

`$ sudo docker-compose up`

Acessar a url que é impressa no terminal geralmente é:
[http://localhost:8000/](http://localhost:8000/)

Admin:
[http://localhost:8000/admin/](http://localhost:8000/admin/)

Para cadastrar novo usuário é necessário entrar no container:
`$ sudo docker exec -it arqsoftware_web_1 /bin/bash`

Rodar:
`$ ./manage.py createsuperuser`
> Em caso de erro rode o comando por extenso: `$ python manage.py createsuperuser`

Usar os dados criado no passo anterior para se logar no admin.