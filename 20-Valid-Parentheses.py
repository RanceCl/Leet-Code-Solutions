'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Assumptions:
1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brack = {
            "(":")",
            "[":"]",
            "{":"}"
        }
        
        # Loop through every character in the given string.
        for i in s:
            # Push open brackets to the top of the stack
            if i in brack: stack.append(i)
            # If an incorrect bracket is encountered, the parentheses aren't valid.
            elif len(stack) == 0 or brack[stack.pop()] != i: return False
        # If the entire string is looped through and the stack is empty, the parentheses are valid.
        return len(stack) == 0
        
