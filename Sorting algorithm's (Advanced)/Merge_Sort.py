def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    L = arr[:mid]
    R = arr[mid:]
    merge_sort(L)
    merge_sort(R)
    return merge(L,R)

def merge(left,right):
    new = []
    i,j = 0,0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new.append(left[i])
            i += 1
        else:
            new.append(right[j])
            j += 1 
        new.extend(left[i:])
        new.extend(right[j:])
        return new 
    
arr = [6,8,8,9,56,345,5432,543]
sort = merge_sort(arr)
print(sort)

