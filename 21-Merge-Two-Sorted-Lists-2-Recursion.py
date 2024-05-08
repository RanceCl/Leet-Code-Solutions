'''
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

This version of the solution used recursion to merge the two lists.

Assumptions:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # When the end of one of the lists is reached, everything in the remaining list can be appended
        if not list1 or not list2: return list1 or list2
        
        # The list 1 value is the next value to be added. 
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        # The list 2 value is the next value to be added. 
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
