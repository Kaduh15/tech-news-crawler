# Tech News Crawler 🕵️‍♂️

Este projeto tem como objetivo principal realizar consultas em notícias sobre tecnologia, obtidas através da raspagem do blog da Trybe. 💻

## Habilidades a serem trabalhadas 💪
    - Utilizar o terminal interativo do Python
    - Escrever seus próprios módulos e importá-los em outros códigos
    - Aplicar técnicas de raspagem de dados
    - Extrair dados de conteúdo HTML
    - Armazenar os dados obtidos em um banco de dados
    
## Requisitos 📌
    - Python 3.x 🐍
    - Docker 🐳 ou mongoDB 💾
    - Bibliotecas especificadas no arquivo dev-requirements.txt 📚
    
## Começando 🚀
Clone o repositório:

```bash
git clone https://github.com/Kaduh15/tech-news-crawler.git
```
### Entre na pasta do repositório:

```bash
cd tech-news-crawler
```

### Crie o ambiente virtual para o projeto:
```bash
python3 -m venv .venv && source .venv/bin/activate
```

### Instale as dependências:
```python
python3 -m pip install -r dev-requirements.txt
```

## Banco de dados 💾
Para a realização deste projeto, será utilizado um banco de dados MongoDB, com nome tech_news. As notícias serão armazenadas em uma coleção chamada news.

### Rodando MongoDB via Docker 🐳

```bash
docker-compose up -d mongodb
```

Para mais detalhes acerca do MongoDB com o Docker, consulte o arquivo docker-compose.yml. 🔍

### Instalando MongoDB nativo
Para instalar e rodar o servidor MongoDB nativo na máquina, siga as instruções nos tutoriais oficiais:

Ubuntu: [Site Oficial](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/) 💻

MacOS: [Site Oficial](https://docs.mongodb.com/guides/server/install/) 💻

Lembre-se de que o MongoDB utilizará a porta 27017 por padrão. Se já houver outro serviço utilizando esta porta, considere desativá-lo.

## Execultando o Projeto 🏃‍♂️
Para rodar o projeto, execute o arquivo principal com o comando `python3 -m tech_news.main`.
