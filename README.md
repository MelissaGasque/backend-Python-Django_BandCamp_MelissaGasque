# BandKamp Generic View
A linguagem utilizada foi Python.
Esse projeto foi desenvolvido com Django, utilizando Generic View, Model Serializer e o Banco de Dados Postgres.  
| Rotas               | Verbo HTTP | Objetivo                        |
|---------------------|------------|---------------------------------|
| /api/users/         | POST       | Registro de usuários            |
| /api/users/pk/      | GET        | Busca por ID de usuários        |
| /api/users/pk/      | PATCH      | Atualização de usuários         |
| /api/users/pk/      | DELETE     | Deleção de usuários             |
| /api/users/login/   | POST       | Login de usuários               |
| /api/albums/        | GET        | Listagem de álbuns              |
| /api/albums/        | POST       | Registro de álbuns              |
| /api/albums/pk/songs/| GET        | Filtragem de músicas            |
| /api/albums/pk/songs/| POST       | Registro de músicas             |
| /api/docs/          | GET        | Documentação Swagger ou Redoc   |  

## Configuração do Ambiente Virtual (Opcional, mas recomendado)
### Crie um ambiente virtual
```
    python -m venv venv
```

### Ative o ambiente virtual
#### No Windows
```
    venv\Scripts\activate
```
#### No Linux/Mac
```
    source venv/bin/activate
```


## Instalar o Django:
```
    pip install django
```

## Instalação das Dependencias
```
    pip install -r requirements.txt
```


## Configuração do banco de dados:
1. Crie um banco de dados PostgreSQL.
2. Copie o arquivo .env.example para .env e configure as variáveis de ambiente relacionadas ao banco de dados.

## Migrações e Aplicações
### Execute as migrações
```
    python manage.py makemigrations
```
```
    python manage.py migrate
```

### Inicie o servidor de desenvolvimento
```
    python manage.py runserver
```




## Preparando ambiente para execução dos testes

1. Verifique se os pacotes **pytest**, **pytest-testdox** e/ou **pytest-django** estão instalados globalmente em seu sistema:
```shell
pip list
```

2. Caso eles apareçam na listagem, rode os comandos abaixo para realizar a desinstalação:

```shell
pip uninstall pytest pytest-testdox pytest-django -y
```

3. Após isso, crie seu ambiente virtual:
```shell
python -m venv venv
```

4. Ative seu ambiente virtual:

```shell
# Linux e Mac:
source venv/bin/activate

# Windows (PowerShell):
.\venv\Scripts\activate

# Windows (GitBash):
source venv/Scripts/activate
```

5. Instale as bibliotecas necessárias:

```shell
pip install pytest-testdox pytest-django
```


## Execução dos testes:
Deste modo, para rodar a bateria de todos os testes, utilize:
```shell
pytest --testdox -vvs
```
---

Caso você tenha interesse em rodar apenas um diretório de testes específico, utilize os comandos abaixo:

Users:
```python
pytest --testdox -vvs tests/users/
```

Albums:
```python
pytest --testdox -vvs tests/albums/
```

Songs:
```python
pytest --testdox -vvs tests/songs/
```

---

Você também pode rodar cada método de teste isoladamente:

```shell
pytest --testdox -vvs caminho/para/o/arquivo/de/teste::NomeDaClasse::nome_do_metodo_de_teste
```

**Exemplo**: executar somente "test_user_login_without_required_fields".

```shell
pytest --testdox -vvs tests/users/test_login_view.py::UserLoginViewTest::test_user_login_without_required_fields
```