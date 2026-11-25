arr = [9, 4, 6, 2, 7]

def insertion_sort(arr):
    shifts = 0
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            current_index = i
            if arr[j] > arr[j+1]:
                current_index = arr[j+1]
                arr[j], arr[j+1] = arr[j+1], arr[j]
                shifts +=1
    print("Sorted array:", arr)
    print("Number of shifts:", shifts)
print(insertion_sort(arr))