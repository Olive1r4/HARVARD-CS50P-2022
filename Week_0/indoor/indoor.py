#Programa solicita uma entrada de string
txt = input()
#Verifica se a string e caixa baixa
if txt.islower():
    #Caso seja caixa baixa, converte para caixa alta
    print(txt.upper())
else:
    #Caso nao seja caixa baixa, converte para caixa baixa
    print(txt.lower())
