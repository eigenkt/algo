# def twoSum(nums, target):
#     # for each number in the lists
#     for i in range(len(nums)):
#     # for each number after it in the list 
#         for j in range(i+1, len(nums)):
#             # if the two numbers add up to a target number then return i and j 
#             if nums[i] + nums[j] == target:
#                 return [i, j]
    #otherwise return an amtpy array 
#     return []

# this above solution takes O(n^2) time and O(1) space

# def twoSum(nums, target):
#     seen = {}
#     # 5:0 3:1 7:2 
#     for i, num in enumerate(nums):
#         diff = target - num
#         if diff in seen:
#             return [seen[diff], i]
#         seen[num] = i

# this solution above takes O(n) time and O(n) space



def twoSum(nums, target):
    nums.sort()
    
    left = 0
    right = len(nums)-1
    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return [left, right]
        elif sum < target:
            left +=1
        else:
            right -= 1
    return []

# This solution has Time Complexity : O(nlogn) 
# and a Space Complexity of O(1)

# nums = [1, 2, 3, 5, 7, 20, 30, 40, 50, 60]
# if we add these two number and the result is equal than the target :
#     return left and right pointer
# if we add these two number and the result is larger than the target :
#     we want to move the rigth pointer in by one
# if we add these two number and the result is smaller than the target :
#     we want to move the left pointer in by one towards the right



numbers = [5, 3, 7, 2, 1, 20, 30, 40, 50, 60]
target = 52
# Time Complexity : O(nlogn) + n  beats n^2 
# Space Complexity 0

# return => 2 and 3
print(twoSum(numbers, target))



# PseudoCode Below for the three solutions

# for i = 0 to n-1:
#     for j = i+1 to n-1:
#         if nums[i] + nums[j] == target:
#             return [i, j]
# return [-1, -1]

# hash_table = {}
# for i = 0 to n-1:
#     if target - nums[i] in hash_table:
#         return [hash_table[target - nums[i]], i]
#     hash_table[nums[i]] = i
# return [-1, -1]

# sort nums
# left = 0
# right = n-1
# while left < right:
#     if nums[left] + nums[right] == target:
#         return [left, right]
#     elif nums[left] + nums[right] < target:
#         left += 1
#     else:
#         right -= 1
# return [-1, -1]
