There are three solutions to the two sum problem 

Solution 1 - Brute force - involves checking every possible pair of elements in the array and seeing if they add up to the target sum. 
It has a time complexity of O(n^2), which is not very efficient for larger arrays

Solution 2 - Hash table - uses using a map to store the elements of the array. We can then check if the target sum minus the current element is in the map. If it is, we have found a pair of elements that add up to the target sum. 
This solution has a time complexity of O(n), which is much more efficient than the brute force approach.

Solution 3 - Sorting and two pointers - by sorting the array and then using two pointers to check if the sum of the elements at the pointers is equal to the target sum. If it is, we have found a pair of elements that add up to the target sum. If it is not, we can move one of the pointers based on whether the sum is too small or too large. 
It has a time complexity of O(nlogn) due to the sorting, but because it does not require additional space for a map thats a trade off that may be worth it.

