import os
from rich import print
from tech_news.menu import analyzer_menu
from tech_news.color_terminal import color_green as cg, color_red as cr


if __name__ == "__main__":
    while True:
        option, func = analyzer_menu()
        os.system('clear') or None
        print(func())
        if option == "5":
            break
        continue_ = input(f'\nDeseja continuar? [{cg("s")}/{cr("n")}]: ')
        os.system('clear') or None
        if continue_.lower() == "n":
            break
