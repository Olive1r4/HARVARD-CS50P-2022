# SYS usado para input por linha de comando
import sys
import random
# Imprime o texto na tela em formato de figlet
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    #Retorna a lista de fonte disponíveis
    figlet = figlet.getFonts()
    # Verifica se o usuário passou um argumento
    if len(sys.argv) == 1:
        # Se não passou argumento usa uma fonte aleatória
        figlet = random.choice(figlet)
        figlet = Figlet(font = figlet)
        inp = input("Input: ")
        print(figlet.renderText(inp))
    # Se o usuário passou um argumento, usa a fonte passada
    elif len(sys.argv) == 3:
        # Verifica de acordo com o exercicio
        if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in figlet:
            # Atribui a fonte passada ao objeto figlet
            figlet = Figlet(font = sys.argv[2])
            inp = input("Input: ")
            print(figlet.renderText(inp))
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
main()