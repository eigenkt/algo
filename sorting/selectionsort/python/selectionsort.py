def selection_sort(arr):
    for i in range(len(arr)):
        # Find the minimum element in the unsorted portion of the array
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the minimum element with the first element of the unsorted portion
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Test the function
arr = [5, 2, 8, 1, 9, 3]
selection_sort(arr)
print(arr)  # Output: [1, 2, 3, 5, 8, 9]
