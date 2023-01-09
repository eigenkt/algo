#include <vector>

void merge_sort(std::vector<int>& arr) {
    // base case: if the length of the array is 1 or less, it's already sorted
    if (arr.size() <= 1) return;

    // split the array into two halves
    size_t half = arr.size() / 2;
    std::vector<int> left(arr.begin(), arr.begin() + half);
    std::vector<int> right(arr.begin() + half, arr.end());

    // recursively sort the two halves
    merge_sort(left);
    merge_sort(right);

    // merge the sorted halves
    merge(arr, left, right);
}

void merge(std::vector<int>& arr, std::vector<int>& left, std::vector<int>& right) {
    // create an iterator for the original array
    std::vector<int>::iterator it = arr.begin();
    
    // while both lists have elements
    while (!left.empty() && !right.empty()) {
        // if the first element of the left list is less than or equal to
        // the first element of the right list, append the left element
        // and remove it from the left list. Otherwise, do the same with the
        // right element.
        if (left.front() <= right.front()) {
            *it = left.front();
            left.erase(left.begin());
        } else {
            *it = right.front();
            right.erase(right.begin());
        }
        ++it;
    }

    // if one list is empty, append all the remaining elements from the other
    // list
    if (!left.empty()) {
        arr.insert(it, left.begin(), left.end());
    } else if (!right.empty()) {
        arr.insert(it, right.begin(), right.end());
    }
