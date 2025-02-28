# Web-Inquérito com Python e Django

## Descrição
Este é um projeto de web-inquérito desenvolvido com Python e Django. O sistema permite responder um inquerito online usado para um tabalho escolar, armazenando os dados em um arquivo csv.

## Uso
- Acesse o inquerito [aqui](https://cristian14.pythonanywhere.com/results)
- Acesse as respostas [aqui](https://cristian14.pythonanywhere.com/survey)

## Tecnologias Utilizadas
- Django
- SQLite (padrão, pode ser substituído por PostgreSQL ou MySQL)
- HTML, CSS e JavaScript para interface

## Funcionalidades
- Exportação dos resultados em CSV

## Como Funciona

O projeto utiliza Django, um framework web baseado em Python, para gerir os página web (webpages). No backend, os modelos do Django definem a estrutura dos dados armazenados no banco de dados, enquanto as views lidam com a lógica de exibição e manipulação das respostas.

Os arquivos principais do projeto incluem:

- `forms.py`: Define as classes que representam os inquéritos e perguntas no banco de dados.
- `views.py`: Contém as funções que controlam a lógica das requisições e respostas do usuário, chamadas views.
- `urls.py`: Mapeia as URLs para as views correspondentes.
- `admin.py`: Configura a interface administrativa do Django para gerenciamento de inquéritos.
- `templates/`: Diretório que contém os arquivos HTML usados para renderizar as páginas do inquérito.

O inquérito consiste num conjunto de perguntas armazenadas no banco de dados, e os utilizadores podem acessá-los via URLs específicas. O Django Admin facilita a criação e administração dos inquéritos, permitindo que os administradores criem inquéritos, editem perguntas e analisem respostas diretamente na interface administrativa.

As respostas submetidas pelos utilizadores são processadas e armazenadas no banco de dados, podendo ser acessadas e exportadas para análise posterior em formatos como CSV. O projeto também utiliza modelos Django para renderizar as páginas.
