# APCPED - Aplicação para publicação de cotações de peças específicas para droids

Projero para gerir criação de demandas de peças.

# Autores:

* **Thiago Pires** - *Desenvolvedor Backend*;

## Requisitos do sistema:

* Python 3.6;
* Django;
* Django Rest Framework;
* PostgreSQL;
* Docker.

## Instalção:

1. Clone o projeto:
```
git clone https://github.com/piresthiago10/APCPED-Finxi.git
```
2. Acesse a pasta APCPED-Finxi e execute o comando:
```
docker-compose up
```

## Executando os testes:

1. Acesse a pasta APCPED-Finxi e execute o comando:
```
sudo docker exec 4e11f1a2f611 python3 manage.py test
```

## Utilizando o projeto:

No arquivo run_web.sh existe a linha de comando com o ip e porta, substitua-os pelos de sua preferência, também os altere 
na collection do Postman e adicione o ip no ALLOWED_HOSTS do settings.py.

run_web.sh:
```
python manage.py runserver 0.0.0.0:8000
```

settings.py:
```
ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'ip de sua preferência']
```

Ao rodar o projeto pela primeira vez será criado o banco de dados, a instalação dos requisitos e um superuser com o username admin e password admin. Utilize-os para acessar o painel de controle em 0.0.0.0:8000/admin crie os usuários comuns para serem os anunciantes.

No Postman, importe a collection através do arquivo finxi.postman_collection.json e na request [post login] insira o username e password de um usuário anunciante criado, a response será o token de acesso desse anunciante.

Em cada uma das requests da collection existe em Headers Key e Value, na Key Autorizathion insira na Value "Token + o token de acesso desse anunciante" (sem aspas).

## Ferramentas utilizadas:

Informe aqui as ferramentas utilizadas para o desenvolvimento do projeto

* [Visual Studio Code](https://code.visualstudio.com/)
* [Google Chrome](https://www.google.pt/intl/pt-PT/chrome/?brand=CHBD&gclid=Cj0KCQjwn_LrBRD4ARIsAFEQFKt3kLTIsdU6a-sk3FKsxrhplkKaYNHo6Pt3aRbaEAJ3TK4fZslZmtUaAvHVEALw_wcB&gclsrc=aw)
