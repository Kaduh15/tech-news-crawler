import sys
from tech_news.analyzer.ratings import top_5_categories
from tech_news.analyzer.search_engine import search_by_category, search_by_date, search_by_title
from tech_news.scraper import get_tech_news



def popula_banco_de_dados():
    amount = int(input('Digite quantas notícias serão buscadas: '))
    get_tech_news(amount)    

def busca_por_titulo():
    titulo = input('Digite o título: ')

    return search_by_title(titulo)

def busca_por_data():
    date = input('Digite a data no formato aaaa-mm-dd: ')

    return search_by_date(date)

def busca_por_categoria():
    categoria = input('Digite a categoria: ')

    return search_by_category(categoria)

def top_5():
    return top_5_categories()

def print_saida():
    return 'Encerrando script'


OPTIONS = {
    0: popula_banco_de_dados,
    1: busca_por_titulo,
    2: busca_por_data,
    3: busca_por_categoria,
    4: top_5,
    5: print_saida
}

# Requisitos 11 e 12
def analyzer_menu():

    option = input(
        'Selecione uma das opções a seguir:\n'
        ' 0 - Popular o banco com notícias;\n'
        ' 1 - Buscar notícias por título;\n'
        ' 2 - Buscar notícias por data;\n'
        ' 3 - Buscar notícias por categoria;\n'
        ' 4 - Listar top 5 categorias;\n'
        ' 5 - Sair.',
    )
    try:
        option = int(option)
        print(OPTIONS[option]())
    except Exception:
        return print('Opção inválida', file=sys.stderr)
    

if __name__ == "__main__":
    analyzer_menu()
