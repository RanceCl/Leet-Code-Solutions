/*
Takes in two integers in the form of reverse order linked lists. 
It will add the two together, with the sum being returned in the same format. 

The digits of the inputs and outputs are in reverse order. Assume that the inputs are non-negative and are not empty.
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(NULLptr) {}
 *     ListNode(int x) : val(x), next(NULLptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummyHead = new ListNode(0);        // A dummy head is used to hold the entire sum to return.
        ListNode* lSum = dummyHead;
        int temp1Val, temp2Val, tempWhole, carry=0;


        /* While loop to add both linked lists. Loop is performed until both lists reach their end. */
        while (l1 != NULL || l2 != NULL || carry != 0)
        {
            // Set the value of the current list element for lists 1 and 2.
            // If an empty value is encountered for a list, set the temporary value to 0
            if(l1 != NULL)
                temp1Val = l1->val;
            else
                temp1Val = 0;
            
            if(l2 != NULL)
                temp2Val = l2->val;
            else
                temp2Val = 0;
            
            //Adding the current values together
            tempWhole = temp1Val + temp2Val + carry;
            
            // Decomposition of the sum into the current position sum and the carry value
            // The carry value is found by removing the last digit of the number
            carry = tempWhole / 10;

            // Place the sum into the next position of the sum linked list and move to the next node
            // The sum for the current position is found by isolating the last digit
            lSum->next = new ListNode(tempWhole%10);
            lSum = lSum->next;

            // Iterate to the next element in the list. Only do this if the end hasn't been reached to prevent error.
            if(l1 != NULL)
                l1 = l1->next;
            if(l2 != NULL)
                l2 = l2->next;
        }
        // At the end, add NULL to indicate the end of the list
        lSum->next = NULL;

        return dummyHead->next;

    }
};
