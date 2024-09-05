import os
import pyfiglet
from colorama import Fore, Style, init

# Inicializa o colorama
init(autoreset=True)

def print_title():   
    """Prints the stylized title of the application."""
    title = 'Text Word Counter'
    figlet_title = pyfiglet.figlet_format(title, font="banner4")
    print(Fore.GREEN + Style.BRIGHT + figlet_title)


def clear_console():
    """Clears the console based on the user's operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')


# gets a list of available fonts
# font_list = pyfiglet.FigletFont.getFonts()
# print(font_list)