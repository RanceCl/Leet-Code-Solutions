'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

This was done using recursive backtracking.
A left bracket could be placed at any point, until the amount of left brackets run out (when left >= n)
A right bracket could only be placed if the amount of right brackets was less than the amount of left (right < left)
When the amount of left and right brackets were both n, the combination could be added.

Assumptions:
1 <= n <= 8
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(validCombo, left, right):
            # We can essentially use left brackets until we run out (when left >= n)
            if left < n: 
                backtrack(validCombo+'(', left+1, right)
            # We can add a right bracket only if there is one open left bracket
            if right < left: 
                backtrack(validCombo+')', left, right+1)
            # When the amount of left and right brackets are n, the combination can be added
            if left == right == n: 
                validCombos.append(validCombo)
            return
        
        validCombos = []
        backtrack('',0,0)
        return validCombos
        
