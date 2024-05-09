'''
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

This version of the solution used a while loop to merge the two lists.

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
        listMerged = listMCurr = ListNode()

        while list1 and list2:
            # Add the lowest value to the list next and move the pointer up for the corresponding list.
            if list1.val <= list2.val: 
                listMCurr.next = list1
                list1 = list1.next
            else: 
                listMCurr.next = list2
                list2 = list2.next
            listMCurr = listMCurr.next
        
        # Add the rest of which ever list remains to the end of the merged list
        if list1: 
            listMCurr.next = list1
        if list2: 
            listMCurr.next = list2
        
        return listMerged.next
