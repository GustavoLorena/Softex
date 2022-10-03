def BubbleSort(lista):
    for bs in range(len(lista)-1, 0, -1):
        for i in range(bs):
            if lista[i] > lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp

lista = [10, 7, 14, 19, 12, 5, 9, 12, 6, 1]
BubbleSort(lista)
print(lista)
