'''
Given an integer x, return true if x is a palindrome, and false otherwise.

This solution would convert the number to a string before comparing the original 
to the reversed string.

Assumptions:
-2^31 <= x <= 2^31 - 1
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers won't be palindromes.
        if x < 0: return False
        return str(x) == str(x)[::-1]
