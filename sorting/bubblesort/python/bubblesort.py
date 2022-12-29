def bubbleSort(arr: list) -> list:
    isSorted = False
    counter = 0
    while not isSorted:
        isSorted = True
        for i in range(len(arr) -1 - counter):
            if arr[i] > arr[i +1]:
                swap(i, i+1, arr)
                isSorted = False
        counter +=1
    return arr

def swap(i:int, j: int, arr: list):
    arr[i], arr[j] = arr[j], arr[i]
            
myArray = [10, 5, 6, 7,  2, 3, 4]
print(bubbleSort(myArray))
