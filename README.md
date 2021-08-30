A equipe de desenvolvimento `Bleeding Edge Enthusiasts` (BEE) se orgulha de usar as tecnologias mais recentes e modernas. Essa regra também se aplica aos projetos desenvolvidos em Python pela equipe BEE.

Para garantir que todos seus projetos em Python estão usando as últimas versões disponíves dos pacotes, a equipe pensou em criar uma ferramenta batizada de MagPy. A ferramenta recebe um nome de projeto, uma lista de pacotes e devolve a última versão de cada pacote.

![Imagem swagger](https://github.com/alexandrabsouz/MagPy/blob/main/img/swagger_magpy.png)
## API MagPy

Para essa solução foi criada a MagPy que gerencia uma coleção de projetos. Cada projeto tem um nome e uma lista de pacotes. Cada pacote tem um nome e uma versão.

O cadastro de um projeto recebe o nome e a lista de pacotes. Cada pacote da lista precisa obrigatoriamente especificar um nome, mas a versão é opcional.

Todos os pacotes informados devem estar cadastrados no PyPI.

Quando o pacote vem apenas com o nome, a API assume que é preciso usar a última versão publicada no PyPI.

## Requisitos

* [Django](https://www.djangoproject.com/);
* [djangorestframework](https://www.django-rest-framework.org/);
* [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/);
* [requests](https://docs.python-requests.org/en/master/);
* [Python3](https://www.python.org/);
* [Python-pip](https://pypi.org/project/pip/);


## Construido com

* [Python](https://www.python.org/) - Linguagem utilizada;
* [Dajngo](https://www.djangoproject.com/) - Framework web utilizado;

## Rodando a API na sua máquina:

O primeiro passo é clonar o repositorio:

```sh
$ git clone https://github.com/alexandrabsouz/MagPy.git
$ cd MagPy
```

Crie um ambiente virtual para instalar dependências e ativá-lo:

```sh
$ pip install python3-venv 
$ python -m venv venv 
$ source venv/bin/activate
```

Intale as dependencias:

```sh
(env)$ pip install -r dev-requirements.txt
```
Observe o `(venv)` na frente do prompt. Isso mostra que o ambiente virtual foi criado pelo `python3-venv`.

Assim que o `pip` terminar de baixar as dependências:
```sh
(venv)$ python manage.py runserver
```
E navegue por `http://127.0.0.1:8000/api/`.


## Uso da API:

Você vai encontrar toda a documentação sobre os endpoints em ![MagPy Swagger](https://instruct-magpy-api.herokuapp.com/swagger/)


## Duvidas

Em caso de duvida, pergunte na seção "Issue". Em caso de erros, poste o motivo e o log para uma melhor resposta!

* [Duvidas](https://github.com/alexandrabsouz/MagPy/issues)

