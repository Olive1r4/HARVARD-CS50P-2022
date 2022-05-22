# Recebe o input do usuário
txt = input()
# Percorre a string
for i in range(len(txt)):
    # Verifica se existe espaco no input digitado
    if txt[i] == " ":
        # Caso exista espaco, substitui por "..."
        print("...", end="")
    else:
        # Caso nao exista espaco, imprime o caractere
        print(txt[i], end="")
print()   

#------------------------------------------------------------------------------
# O mesmo codigo em duas linhas
txt1 = input()
print(txt1.replace(" ", "..."))