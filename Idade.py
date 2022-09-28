from datetime import date
current_date = date.today()
anoAtual = current_date.year

date = True
while (date == True):
    nome = input("Informe seu nome completo: ")

    try:
        anoNasc = int(input("Informe o ano que você nasceu (4 dígitos):"))
        idade = anoAtual - anoNasc
        if (anoNasc >= 1922 and anoNasc <= 2021):

            date = False

            print(nome, "possuirá ", idade,
                  "anos no ano de ", current_date.year, ".")
            break

        else:
            print("A data informada está incorreta!")

    except:
        print("Caracter inválido, por favor digite um ano válido.")
