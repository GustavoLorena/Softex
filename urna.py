def votacao(candidato):
    global candidato889, candidato847, candidato515
 
    if candidato.isalpha():
        if candidato == 'Fim' or candidato == 'fim' or candidato == 'FIM':
            print('FIM DA VOTAÇÃO')
            print_resultados()

    elif candidato.isnumeric():
        if candidato == '889' or candidato == '847' or candidato == '515':
            if candidato == '889':
                candidato889 += 1
            elif candidato == '847':
                 candidato847 += 1
            elif candidato == '515':
                 candidato515 += 1
        else:
            candidato= str(input('Digite um numero valido para o candidato: '))
            votacao(candidato)


def print_resultados():
    global candidato889, candidato847, candidato515

    print('QUANTIDADE DE VOTOS:\n')
    print('CANDIDATO NÚMERO 889 - TOTAL DE ' + str(candidato889))
    print('CANDIDATO NÚMERO 847 - TOTAL DE ' + str(candidato847))
    print('CANDIDATO NÚMERO 515 - TOTAL DE ' + str(candidato515))

    exit()  

if __name__ == '__main__':
    candidato889 = 0
    candidato847 = 0
    candidato515 = 0

    while True:
        candidato = str(input('ELEIÇÃO \nCandidado 889\nCandidato 847\nCandidato 515\nFim para encerrar\nDigite o numero do seu candidato: '))
        votacao(candidato)
