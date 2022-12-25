// Brute force solution:
// This solution involves checking every possible pair of numbers in the given array and returning the indices of the two numbers that sum to the target value
// This solution has a time complexity of O(n^2) as it involves nested loops.

// 
vector<int> twoSum(vector<int>& nums, int target) {
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            if (nums[i] + nums[j] == target) {
                return {i, j};
            }
        }
    }
    return {};
}


// Hash table solution:
// This solution involves using a hash table to store the values of the array as keys and their indices as values. Then, for each element in the array, we can check if the hash table contains the target value minus the current element. If it does, we return the indices of the current element and the element in the hash table.

vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> hash;
    for (int i = 0; i < nums.size(); i++) {
        int complement = target - nums[i];
        if (hash.count(complement) && hash[complement] != i) {
            return {i, hash[complement]};
        }
        hash[nums[i]] = i;
    }
    return {};
}

// Sorting and two pointers solution:
// This solution involves sorting the array and then using two pointers to check for the pair of numbers that sum to the target value. We start by setting the left pointer to the first element and the right pointer to the last element of the sorted array. If the sum of the elements pointed to by the left and right pointers is less than the target value, we move the left pointer to the next element. If the sum is greater than the target value, we move the right pointer to the previous element. If the sum is equal to the target value, we return the indices of the elements pointed to by the left and right pointers.


vector<int> twoSum(vector<int>& nums, int target) {
    vector<int> numsSorted(nums);
    sort(numsSorted.begin(), numsSorted.end());

    int left = 0;
    int right = numsSorted.size() - 1;
    while (left < right) {
        int sum = numsSorted[left] + numsSorted[right];
        if (sum == target) {
            break;
        }
        else if (sum < target) {
            left++;
        }
        else {
            right--;
        }
    }

    vector<int> indices;
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] == numsSorted[left] || nums[i] == numsSorted[right]) {
            indices.push_back(i);
        }
   
