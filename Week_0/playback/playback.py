#Recebe um input do usuario
txt = input()
#Percorre a string e verifica sem tem espaço
for i in range(len(txt)):
    #Se tiver espaço, substitui por "..."
    if txt[i] == " ":
        print("...", end="")
    else:
        #Se não tiver espaço, imprime o valor até acabar a string
        print(txt[i], end="")
print()