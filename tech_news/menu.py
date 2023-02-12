import os
from tech_news.analyzer.ratings import top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_date,
    search_by_title,
)
from tech_news.color_terminal import color_red as cr, color_yellow as cy
from tech_news.database import find_news
from tech_news.scraper import get_tech_news


def popula_banco_de_dados():
    os.system('clear') or None
    amount = int(input("Digite quantas notícias serão buscadas: "))
    os.system('clear') or None
    print(f'Buscando todas as {amount} notícias, aguarde...')
    get_tech_news(amount)
    return 'Busca finalizada'


def busca_por_titulo():
    titulo = input("Digite o título: ")
    result = search_by_title(titulo)
    text = f'\n {"RESULTADO DA BUSCA POR TITULO"} \n\n'
    for news in result:
        text += f'{news[0]} -> {news[1]} \n\n'
    return text


def busca_por_data():
    date = input("Digite a data no formato aaaa-mm-dd: ")
    result = search_by_date(date)
    text = f'\n {"RESULTADO DA BUSCA POR TITULO"} \n\n'
    for news in result:
        text += f'{news[0]} -> {news[1]} \n\n'
    return text


def busca_por_categoria():
    news = find_news()
    categories = set([news["category"] for news in news])
    print(categories)
    categoria = input("Digite uma das categorias a cima: ")
    result = search_by_category(categoria)
    text = f'\n {cy("RESULTADO DA BUSCA POR CATEGORIA")} \n\n'
    for news in result:
        text += f'{news[0]} -> {news[1]} \n\n'
    return text


def top_5():
    return top_5_categories()


def print_saida():
    return "Encerrando script"


OPTIONS = {
    '0': popula_banco_de_dados,
    '1': busca_por_titulo,
    '2': busca_por_data,
    '3': busca_por_categoria,
    '4': top_5,
    '5': print_saida,
}


# Requisitos 11 e 12
def analyzer_menu():
    option = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por categoria;\n"
        " 4 - Listar top 5 categorias;\n"
        " 5 - Sair.\n"
        "Digite um valor entre 0 e 5: "
    )

    while not (option in OPTIONS):
        print(f'{cy("Opção inválida")} texto digitado: {cr(option)}')
        option = input(
            f'Digite um valor entre {cy("0")} e {cy("5")}: '
        )

    return [option, OPTIONS[option]]
