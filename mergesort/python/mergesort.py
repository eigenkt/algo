def merge_sort(arr):
    # base case: if the length of the array is 1 or less, it's already sorted
    if len(arr) <= 1:
        return arr

    # split the array into two halves
    half = len(arr) // 2
    left = arr[:half]
    right = arr[half:]

    # recursively sort the two halves
    left = merge_sort(left)
    right = merge_sort(right)

    # merge the sorted halves
    return merge(left, right)

def merge(left, right):
    # create an empty list to store the merged list
    merged = []
    
    # while both lists have elements
    while left and right:
        # if the first element of the left list is less than or equal to
        # the first element of the right list, append the left element
        # and remove it from the left list. Otherwise, do the same with the
        # right element.
        if left[0] <= right[0]:
            merged.append(left[0])
            left.pop(0)
        else:
            merged.append(right[0])
            right.pop(0)

    # if one list is empty, append all the remaining elements from the other
    # list
    if left:
        merged += left
    if right:
        merged += right

    return merged
