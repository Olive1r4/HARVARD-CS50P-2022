def main():
    product = get_item()
    # percorre o dicinário em ordem alfabética e imprime a quantidade de cada item e nome
    for key in sorted(product):
        print(product[key], key)

def get_item():
    # Cria um dicionário vazio
    products = {}
    while True:
        try:
            item = input().upper()
            # Se o item não estiver no dicionário, adiciona-o com a quantidade 1
            if item in products:
                products[item] += 1
            # Se o item estiver no dicionário, adiciona +1 na quantidade
            else:
                products[item] = 1
        # Se o usuário digitar control+d, o loop é interrompido
        except EOFError:
            return products
main()