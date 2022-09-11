import inflect

def main():
    # Create a pluralizer object
    p = inflect.engine()
    nameList = []
    while True:
        try:
            name = input("Name: ").title()
            if name not in nameList:
                nameList.append(name)
        # Verifica se o valor digitado corresponde ao que for pedido
        except ValueError:
            pass
        # If user end input(ex. control+d) without reading any data the method will return an empty string
        except EOFError:
            print()
            # Imprime a lista como um texto "palavra, palavra, palavra e palavra"
            print(f"Adieu, adieu, to {p.join(nameList)}")
            break
main()