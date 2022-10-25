def calculadora():
    operacao = input('''
Por favor escolha com qual operador você deseja trabalhar
1 para adição
2 para subtração
3 para multiplicação
4 para divisão
''')

    if operacao == '1':
        n1 = int(input("Insira o primeiro número: "))
        n2 = int(input("Insira o segundo número: "))
        print('{} + {} = '.format(n1, n2))
        print(n1 + n2)

    elif operacao == '2':
        n1 = int(input("Insira o primeiro número: "))
        n2 = int(input("Insira o segundo número: "))
        print('{} - {} = '.format(n1, n2))
        print(n1 - n2)

    elif operacao == '3':
        n1 = int(input("Insira o primeiro número: "))
        n2 = int(input("Insira o segundo número: "))
        print('{} * {} = '.format(n1, n2))
        print(n1 * n2)

    elif operacao == '4':
        n1 = int(input("Insira o primeiro número: "))
        n2 = int(input("Insira o segundo número: "))
        print('{} / {} = '.format(n1, n2))
        quociente = n1 // n2
        print('Seu quociente é ', quociente)
        resto = n1 % n2
        print('E seu resto ', resto)

    else:
        print("Você não escolheu um operador válido")
        exit()


calculadora()
