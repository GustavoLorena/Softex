def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1       
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key


data = [1,5,3,8,9,12,31,65,98,25,36,74,54,25,7,4,21,35,42,14,27,29,15,32,24,2,6,34,13,18]
insertionSort(data)
print(data)
