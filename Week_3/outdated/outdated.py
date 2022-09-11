def main():
    date = get_date()
    print(f"{date}")

def get_date():
    month = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    while True:
        try:
            # Recebe um imput do usuário e retira os espaços em branco
            date = input("Date: ").replace(" ", "")
            # Procura por "/" no input e se houver ele divide o input em duas partes
            if date.find('/') != -1:
                date = date.split('/')
                m = int(date[0])
                d = int(date[1])
                y = int(date[2])
                # Verifica se o mês é válido de acordo com o problema do exercício
                if m in range(1, 13) and d in range(1, 32) and y > 0:
                    # retorna a data de acordo com o formato do exercício
                    # O ":02" significa que o número deve ter 2 dígitos se não tiver ele adiciona um 0 antes
                    return (f"{y:04}-{m:02}-{d:02}")

            elif date.find(",") != -1:
                date = date.split(",")
                m = date[0]
                m = m[:-1].title()

                d = date[0]
                d = int(d[-1])

                y = int(date[1])

                if m in month and d in range(1, 32) and y > 0:
                    # retorna a posição do mês no array de meses e adiciona +1 para que o número seja correto, já que o array começa em 0
                    m = month.index(m) + 1
                    # retorna a data de acordo com o formato do exercício
                    # O ":02" significa que o número deve ter 2 dígitos se não tiver ele adiciona um 0 antes
                    return (f"{y:04}-{m:02}-{d:02}")
        except ValueError:
            pass

main()