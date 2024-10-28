# Python-Web-Django
### Desenvolvimento web com django

Este é um projeto de blog desenvolvido com Django. 
O blog permite que os usuários adicionem e gerenciem postagens de forma simples e eficiente.


#### Funcionalidades

Criação e gerenciamento de postagens.
URLs amigáveis com o uso de slugs.
Interface de administração do Django para gerenciar conteúdo.

#### Requisitos

    Python 3.12.6
    Django 5.1.2
    Database sqlite3

Instalação

##### 1.Clone o repositório:

`git clone https://github.com/alexpaulo100/python-web-django.git`

cd "seu-repositorio"


##### 2.Crie um ambiente virtual e ative-o:

Em Linux use:

`python -m venv venv`
`source venv/bin/activate`  

Em Windows use: 

`venv\Scripts\Activate.ps1`

##### 3.Instale as dependências:

`pip install -r requirements.txt`

##### 4.Execute as migrações:

`django-admin migrate`

##### 5.Inicie o servidor:
`django-admin runserver`


##### Método 2: Usando Docker

Se você preferir usar Docker, siga os passos abaixo:

Clone o repositório (se ainda não o fez):

`git clone https://github.com/alexpaulo100/python-web-django.git`

cd "seu-repositorio"

Construa e inicie os containers:

`docker-compose up --build`

Execute as migrações:

`docker-compose exec django python manage.py migrate --noinput`

Acesse o aplicativo: O aplicativo estará disponível em http://localhost.

#### Comandos extras para usar em Linha de Comando

Este projeto inclui um comando personalizado para adicionar novas postagens ao banco de dados diretamente pela linha de comando.
Uso

Para adicionar um novo post, utilize o seguinte comando:
$ django-admin add_post --title "Titulo" --content "Conteúdo" 
    
- --title: O título da postagem (obrigatório).
- --content: O conteúdo da postagem (obrigatório).


#### Linter

Este projeto utiliza o Ruff como linter para garantir a qualidade do código. 
Para verificar o código, execute:
`ruff check django`
`ruff format djando`

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)


Licença

Este projeto está licenciado sob a MIT License.

