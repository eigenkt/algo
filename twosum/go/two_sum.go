package main 

func main() {
  nums := []int{10,30,98,70,20,40}
  target = 60
  two_sum(nums, target)
}

func two_sum(nums []int, target int) []int {
    for i := 0; i < len(nums); i++ {
        for j := i + 1; j < len(nums); j++ {
            if nums[i] + nums[j] == target {
                return []int{i, j}
            }
        }
    }
    return []int{}
}


func two_sum(nums []int, target int) []int {
    numsMap := make(map[int]int)
    for i, num := range nums {
        complement := target - num
        if idx, ok := numsMap[complement]; ok {
            return []int{idx, i}
        }
        numsMap[num] = i
    }
    return []int{}
}

func two_sum(nums []int, target int) []int {
    numsSorted := make([]int, len(nums))
    copy(numsSorted, nums)
    sort.Ints(numsSorted)

    left := 0
    right := len(numsSorted) - 1
    for left < right {
        sum := numsSorted[left] + numsSorted[right]
        if sum == target {
            break
        } else if sum < target {
            left++
        } else {
            right--
        }
    }

    indices := []int{}
    for i, num := range nums {
        if num == numsSorted[left] || num == numsSorted[right] {
            indices = append(indices, i)
        }
    }
    return indices
}
