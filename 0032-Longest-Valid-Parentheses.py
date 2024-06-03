'''
Given a string containing just the characters '(' and ')', return the length 
of the longest valid (well-formed) parentheses 
substring.

The initial index stored in the stack is -1. This allows for easy math 
in the instance that a valid parentheses set starts at the beginning of 
the string. 

Whenever an open parenthesis is encountered, its index will be appended to 
the end of the stack, indicating that it is waiting to be closed.

If a closed parenthesis is encountered, the index of the last encountered 
open parenthesis will be popped from the stack. Two things can occur from 
here, depending on if this closed parenthesis was closing an already stored 
open parenthesis stored in the stack:
    If the stack is empty, that means that were no open parentheses before 
    this closed one that were valid to close it, popping the initial dummy 
    head. 
    The index of this invalid closed parenthesis will be stored to be the 
    new index to be compared against. 

    If the stack wasn't empty, then the encountered closed parenthesis 
    closed a waiting open parenthesis, with the current character's index 
    being compared to the new tail of the stack to find the length of the 
    current substring of valid parentheses. 
    This value will be compared to the currently stored substring length to 
    determine which is longest. 

Whatever length stored by the end is the length of the longest valid 
parentheses substring. 

Assumptions: 
0 <= s.length <= 3 * 10^4
s[i] is '(', or ')'.
'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Initial index to be compared against is -1 for math. 
        stack = [-1]
        maxParenLength = 0

        # Loop through every character in the given string.
        for i in range(len(s)):
            # Push open brackets to the top of the stack
            if s[i] == '(': 
                stack.append(i)
            # Closed bracket encountered
            else: 
                # If ) encountered, pop the corresponding (.
                stack.pop()
                
                # If the stack is empty, push a new starting index
                if not stack:
                    stack.append(i)
                
                # The ) closed a waiting (, update length
                else: 
                    # Substring end is the last stored index in stack.
                    maxParenLength = max(maxParenLength, i - stack[-1])
        return maxParenLength
