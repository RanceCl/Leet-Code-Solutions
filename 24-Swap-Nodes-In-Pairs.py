'''
Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes 
(i.e., only nodes themselves may be changed.)

Assumptions: 
The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100

Here is an example of how the swapping algorithm works
p -> c
0 -> 1 -> 2 -> 3 -> 4

Switch 2 and 3
    p = 1 -> 2 -> 3 -> 4    c = 2 -> 3 -> 4
1.  Make 1's next pointer point to 3
    p = 1 -> 3 -> 4         c = 2 -> 3 -> 4
    Now 1's next is pointing to the right node, 
    but 3's next is pointing to the wrong one
    
2.  Make 2's next pointer point to 4
    p = 1 -> 3 -> 4         c = 2 -> 4
    Now 2's next is pointing to the right node

3.  Make 3's next pointer point to 2
    p = 1 -> 3 -> 2 -> 4    c = 2 -> 4
    Now 3's next is pointing to the right node
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        prev, curr = dummy, head

        while curr and curr.next:
            # Switch two nodes
            prev.next = curr.next
            curr.next = curr.next.next
            prev.next.next = curr
            
            # Shift to the next pair to be swapped.
            prev = curr
            curr = curr.next
        return dummy.next
