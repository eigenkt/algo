package main

import "fmt"

// HeapSort sorts an array using the heap sort algorithm
func HeapSort(arr []int) {
    // First, we build a max heap from the array
    n := len(arr)
    for i := n/2 - 1; i >= 0; i-- {
        heapify(arr, n, i)
    }
    // Next, we repeatedly extract the maximum element from the heap
    // and place it at the end of the array
    for i := n - 1; i >= 0; i-- {
        // Move the current root to the end
        arr[i], arr[0] = arr[0], arr[i]
        // Call heapify on the reduced heap
        heapify(arr, i, 0)
    }
}

// heapify is a helper function that transforms a semi-heap into a max heap
func heapify(arr []int, n int, root int) {
    // Assume the root is the largest element
    largest := root
    left := 2*root + 1
    right := 2*root + 2

    // Check if the left child is larger than the root
    if left < n && arr[left] > arr[largest] {
        largest = left
    }

    // Check if the right child is larger than the root
    if right < n && arr[right] > arr[largest] {
        largest = right
    }

    // If the largest element is not the root, swap and heapify the subtree
    if largest != root {
        arr[root], arr[largest] = arr[largest], arr[root]
        heapify(arr, n, largest)
    }
}

func main() {
    arr := []int{3, 2, 1, 5, 6, 4}
    HeapSort(arr)
    fmt.Println(arr)
    // Output: [1 2 3 4 5 6]
}
