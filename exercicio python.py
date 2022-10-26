def Notas ():
    n1 = int(input("Insira o primeira nota: "))
    n2 = int(input("Insira o segunda nota: "))
    media = (n1+n2)/2
    print('Sua média é ', media)
    if media <= 7:
        x = 21
        
        print('Aluno Reprovado')
    else:
        print('Aluno aprovado')
Notas()
