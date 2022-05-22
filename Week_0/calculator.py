# Convertento o input para int
x = int(input("What's X? "))
y = int(input("What's Y? "))

print(f"{x} + {y} = {x + y}")
# Convertendo o input dentro da funao do print
#print(f"{x} + {y} = {int(x) + int(y)}")

x = float(input("What's X? "))
y = float(input("What's Y? "))

# Arredondando o resultado para cima
z = round(x + y)
print(z)

x = float(input("What's X? "))
y = float(input("What's Y? "))

# Arredondando o resultado para dois digitos depois da virgula
z = round(x / y, 2)
print(z)


# Outra forma de arredondar
#z = (x / y)
#print(f"{z:.2f}")
