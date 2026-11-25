import random
arr = random.sample(range(1, 101), 20)


def bubble_sort(arr):
    passes = 0
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(arr)
        passes +=1
    print(passes)    
    print("sorted array:", arr)


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

print(bubble_sort(arr))
print(insertion_sort(arr))
print(selection_sort(arr))