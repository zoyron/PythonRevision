# bubble sort implementation in python. this will be the optimized version of the algorithm
# this will directly be the optimized bubble sort algorithm

def bubbleSort(arr):
    swapped = 0
    n = len(arr)
    for i in range(n-1, -1, -1):
        for j in range(0, i):
            if(arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swapped+=1
        if swapped:
            break





arr = []
n = int(input())
for i in range(n):
    x = int(input())
    arr.append(x)
print(arr)
bubbleSort(arr)
print(arr)
# yay the bubble sort implementation in python worked too, now I understand it a bit better
