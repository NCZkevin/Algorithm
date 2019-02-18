#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (30.48%)
# Total Accepted:    754.4K
# Total Submissions: 2.5M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Example:
# 
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        re = ListNode(0)
        r=re
        carry=0
        while(l1 or l2):
            x= l1.val if l1 else 0
            y= l2.val if l2 else 0
            s=carry+x+y
            carry=s//10
            r.next=ListNode(s%10)
            r=r.next
            if(l1!=None):l1=l1.next
            if(l2!=None):l2=l2.next
        if(carry>0):
            r.next=ListNode(1)
        return re.next   

        # ans = ListNode(0)
        # tmp = ans
        # tmpsum = 0
        # while True:
        #     #依次遍历l1 l2，对应位相加
        #     if l1 != None:
        #         tmpsum += l1.val
        #         l1 = l1.next
        #     if l2 != None:
        #         tmpsum += l2.val
        #         l2 = l2.next
        #     tmp.val = tmpsum % 10     # 除10取余作为当前位的值
        #     tmpsum //= 10                #除10取整，即高位，作为指针的下个结点 进行加法运算
        #     if l1 == None and l2 == None and tmpsum == 0:
        #         break
        #     tmp.next = ListNode(0)
        #     tmp = tmp.next
        # return ans
