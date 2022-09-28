def soma ():
    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))
    print("A soma é: ",x+y)
    print(" ")
    
def subtracao():
    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))
    print("A subtração é: ",x-y)
    print(" ")

def multiplicacao():
    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))
    print("A multipiclação é: ",x*y)
    print(" ")
    
def divisao ():
    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))
    print("A divisão é: ",x/y)
    print(" ")
    
opcao=1

while opcao:
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Sair")
        
    opcao = int(input("Escolha a opção: "))
    
    if (opcao == 1):
        soma()
    if (opcao == 2):
        subtracao()
    if (opcao == 3):
        multiplicacao()
    if (opcao == 4):
        divisao()
