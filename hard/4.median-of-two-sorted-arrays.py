#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (25.39%)
# Total Accepted:    378K
# Total Submissions: 1.5M
# Testcase Example:  '[1,3]\n[2]'
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# 
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).
# 
# You may assume nums1 and nums2 cannot be both empty.
# 
# Example 1:
# 
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# The median is 2.0
# 
# 
# Example 2:
# 
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# The median is (2 + 3)/2 = 2.5
# 
# 
#
class Solution:
    def findMedianSortedArrays(self, nums1: 'List[int]', nums2: 'List[int]') -> 'float':

        # num = nums1 + nums2
        # num.sort()
        # m = int(len(num)/2)
        # if len(num) % 2 ==0:
        #     return (num[m] + num[m-1])/2
        # else:
        #     return num[m]

        length1 = len(nums1)
        length2 = len(nums2)
        k = (length1 + length2) // 2
        if (length1 + length2) % 2 == 0:
            return (self.findK(nums1, nums2, k) + self.findK(nums1, nums2, k - 1)) / 2.0;   # 2 is enough in python3
        else:
            return self.findK(nums1, nums2, k)

    def findK(self, num1, num2, k):
        # Recursive ends here
        if not num1:
            return num2[k]
        if not num2:
            return num1[k]
        if k == 0:
            return min(num1[0], num2[0])

        length1 = len(num1)
        length2 = len(num2)
        if num1[length1 // 2] > num2[length2 // 2]:
            if k > length1 // 2 + length2 // 2:
                return self.findK(num1, num2[length2 // 2 + 1:], k - length2 // 2 - 1)
            else:
                return self.findK(num1[:length1 // 2], num2, k)
        else:
            if k > length1 // 2 + length2 // 2:
                return self.findK(num1[length1 // 2 + 1:], num2, k - length1 // 2 - 1)
            else:
                return self.findK(num1, num2[:length2 // 2], k)
