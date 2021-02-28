#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 1. iteratively reverse
        # prev, curr = None, head
        # while curr:
        #     next = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = next
        # return prev

        # 2. recursively reverse
        if head is None or head.next is None:
            return head
    
        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return node
             
# @lc code=end

