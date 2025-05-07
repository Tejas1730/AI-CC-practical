def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i 
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:  
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"Step {i+1}: {arr}")

arr = list(map(int, input("Enter numbers separated by space: ").split()))
print("\nOriginal Array:", arr)
selection_sort(arr)
print("\nSorted Array:", arr)


'''
Selection Sort – Theory
🎯 Goal:
Sort an array by repeatedly selecting the minimum (or maximum) element from the unsorted part and putting it at the beginning (or end).

Key Idea:
Divide the array into sorted and unsorted parts.

Repeatedly pick the minimum element from the unsorted part.

Swap it with the first unsorted element.

Move the boundary of the sorted section by one

for i = 0 to n-1:
    min_index = i
    for j = i+1 to n-1:
        if array[j] < array[min_index]:
            min_index = j
    swap array[i] and array[min_index]

O(n²)
'''