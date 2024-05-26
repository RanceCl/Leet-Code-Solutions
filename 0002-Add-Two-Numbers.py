'''
Takes in two integers in the form of reverse order linked lists. 
It will add the two together, with the sum being returned in the same format. 

The digits of the inputs and outputs are in reverse order.
Assume that the inputs are non-negative and are not empty.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0) # A dummy head is used to hold the entire sum to return.
        lSum = dummyHead
        carry=0

        # Temporary holders for the current position of the input lists
        temp1 = l1
        temp2 = l2

        ''' While loop to add both linked lists. Loop is performed until both lists reach their end. '''
        while (temp1 != None or temp2 != None or carry != 0):
            # Set the value of the current list element for lists 1 and 2.
            # If an empty value is encountered for a list, set the temporary value to 0
            if temp1 != None:
                temp1Val = temp1.val
            else:
                temp1Val = 0
            
            if temp2 != None:
                temp2Val = temp2.val
            else:
                temp2Val = 0
            
            #Adding the current values together
            tempWhole = temp1Val + temp2Val + carry
            
            # Decomposition of the sum into the current position sum and the carry value
            # The carry value is found by removing the last digit of the number
            # The sum for the current position is found by isolating the last digit
            carry = tempWhole // 10

            # Place the sum into the next position of the sum linked list and move to the next node
            lSum.next = ListNode(tempWhole % 10)
            lSum = lSum.next

            # Iterate to the next element in the list. Only do this if the end hasn't been reached to prevent error.
            if temp1 != None:
                temp1 = temp1.next
            if temp2 != None:
                temp2 = temp2.next
        
        # At the end, add None to indicate the end of the list
        lSum.next = None

        return dummyHead.next

