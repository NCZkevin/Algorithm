package leetcode

func findUnsortedSubarray(nums []int) int {
    n := len(nums)
    l,r := 0,n-1
    max,min := nums[0],nums[n-1]
    for i :=1;i<n;i++ {
        if nums[i] >= max {
            max = nums[i]
        } else {
            l = i
        }
    }
    for i:=n-1;i>=0;i-- {
        if nums[i] > min {
            r = i
        } else {
            min = nums[i]
        }
    }
    if r - l + 1 == n {
        return 0
    } else {
        return l - r + 1
    }
}