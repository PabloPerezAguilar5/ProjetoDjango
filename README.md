# Projeto de gerenciamento de estoque de instrumentos musicais

Este projeto é uma aplicação web de gerenciamento de estoque para uma loja de instrumentos musicais. Ele usa Django como framework principal e oferece funcionalidade para carregar dados de um arquivo Excel, gerenciar produtos por meio de um painel de administração personalizado e visualizar estatísticas em um painel.

## Características

- **Data Loader**: Implementado um comando personalizado para carregar dados de um arquivo Excel usando a biblioteca `pandas`. Este comando lê um arquivo contendo o estoque da loja e o importa para o banco de dados.

- **API simulada**: uma API simulada foi criada utilanzado Django RestFramework para facilitar a interação com os dados do produto. Isso permite testar e demonstrar o aplicativo sem depender de um banco de dados em produção.

- **AdminSite Personalizado**: Um painel de administração personalizado foi desenvolvido utilizando a classe `AdminSite` do Django, permitindo um melhor gerenciamento do produto. Inclui opções para editar, excluir e pesquisar produtos com eficiência.

- **Dashboard**: Foi implementado um dashboard que apresenta estatísticas de estoque, mostrando a quantidade de produtos por categoria, que fornece uma visão geral do estoque disponível na loja.

## Tecnologias usadas

- **Django**: Framework de desenvolvimento web em Python.
- **Pandas**: Biblioteca de análise de dados usada para ler e processar o arquivo Excel.
- **SQLite**: Banco de dados usado para armazenar dados de produtos.
- **HTML**: Para o design da interface do usuário do painel de administração e do dashboard.
- **aiohttp**: Para fazer chamadas assíncronas para a API externa.

## Instalação
Clone o repositório:  `git clone https://github.com/pabloperezaguilar5/ProjetoDjango.git`.
1. Clone o repositorio:

   ```bash
   git clone https://github.com/pabloperezaguilar5/ProjetoDjango.git

2. instale os requisitos:
```
pip install -r requirements.txt
```
3. Execute as migrações:
```
python manage.py migrate
 ```
4. Execute o servidor:
```
python manage.py runserver
```
5. Execute o comando de carregamento de dados:
```
python manage.py load_data
```
6. Acessar o administrador personalizado
```
http://127.0.0.1:8000/custom-admin/
```
7. Accesar o dashboard:
```
http://127.0.0.1:8000/custom-admin/dashboard/
```


