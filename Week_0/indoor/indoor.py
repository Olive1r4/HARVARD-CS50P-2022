#recebe um input do usuário e retorna o valor digitado
txt = input()
# verifica se o valor digitado está em caixa baixa
if txt.islower():
    # se estiver em caixa baixa, converte para caixa alta
    print(txt.upper())
else:
    # se não estiver em caixa baixa, imprime o valor digitado
    print(txt.lower())