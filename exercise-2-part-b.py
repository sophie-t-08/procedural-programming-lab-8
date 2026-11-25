arr = [25, 64, 11, 22, 12]

def selection_sort(arr):
   shifts = 0
   for i in range(len(arr)):
    min_idx = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
    shifts +=1
    print(arr)
    print(shifts)
print(selection_sort(arr))