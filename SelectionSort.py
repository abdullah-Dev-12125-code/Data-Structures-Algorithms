def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        mini = i
        for j in range(i+1,n):
            if arr[i] > arr[j]:
                mini = j
                arr[i],arr[mini] = arr[mini],arr[i]

array = [23,0,76,43,3]
selection_sort(array)
print(array)