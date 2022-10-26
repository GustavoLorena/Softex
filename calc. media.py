def Notas():
    n1 = int(input("Insira o primeira nota: "))
    n2 = int(input("Insira o segunda nota: "))
    media = (n1+n2)/2
    print('Sua média é ', media)
    if media <= 7:
        print('Aluno Reprovado')
        rest = 14 - media
        print('O aluno precisa tirar', rest, 'na recuperação para passar!')
    else:
        print('Aluno aprovado')


Notas()
