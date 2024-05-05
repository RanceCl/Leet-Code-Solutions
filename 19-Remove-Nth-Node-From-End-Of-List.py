'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

This was done with two pointers. 
One was updated ahead by n steps. Using this one to find the end of the list and updating the second
pointer at the same time, the second pointer's next node would be the one that we needed to remove. 

Assumptions:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        behindNode = aheadNode = head

        # Pointer that will reach the end of the list.
        for _ in range(n): aheadNode = aheadNode.next

        # If the head needs to be removed.
        if not aheadNode: return head.next

        # Loop until the ahead node reaches the end, which will prepare the current node for removal.
        while aheadNode.next is not None: behindNode, aheadNode = behindNode.next, aheadNode.next
        
        # Remove the desired node.
        behindNode.next = behindNode.next.next

        return head
