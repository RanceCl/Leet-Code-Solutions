'''
Given an integer x, return true if x is a palindrome, and false otherwise.

This solution would use a while loop to reverse the number. 

Assumptions:
-2^31 <= x <= 2^31 - 1
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers won't be palindromes.
        if x < 0: return False
        
        xtemp, xrev = x, 0
        # Reverse the number
        while xtemp > 0:
            xrev = xrev*10 + xtemp%10
            xtemp //= 10
        return x == xrev
        
