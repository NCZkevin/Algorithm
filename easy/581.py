class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0,n-1
        big,small = nums[0],nums[-1]
        for i in range(1,n):
            if nums[i] < big:
                l = max(l,i)
            else:
                big = nums[i]
        for i in range(n-1,-1,-1):
            if nums[i] > small:
                r = min(r,i)
            else:
                small = nums[i]
        if r-l+1 == n: return 0
        return l-r+1

