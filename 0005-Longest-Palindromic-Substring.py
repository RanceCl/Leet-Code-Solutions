'''
Given a string s, the longest panindromic substring within 
s was returned.

The method used was to go through every character in s and 
expand around this center character to find the longest 
palindrome around it. Since the substring could be odd or 
even, this was done twice for each character, once with 
the center being the character at index i, and the second 
time being done with the characters at index i and i+1.

Once this new substring was found, it's length would be  
compared to the currently stored longest substring.

This was repeated until all characters as centers were 
exhausted, with the final substring stored being the 
longest in s. 

It should be noted that placing the length comparison if 
statement into the expansion function could allow for a 
slightly more memory efficient solution. However, the 
helper function is useful enough on its own, so this 
separation was done for modularity. 
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # Expand the substring from the center index until the palidrome ends or an edge is reached.
        def findPalindromeSubstringFromCenter(left, right, s):
            # Loop will continue until the string's edge is reached or the palindrome ends.
            while left>=0 and right<len(s) and s[left]==s[right]:
                left -= 1
                right += 1
            # New palindrome substring
            return s[left + 1:right]
        
        longPal = s[0]
        # Loop through every character in string s to use each as a center. 
        for i in range(len(s)-1):
            # Expand substring twice from 'i', since the palindromic substring could be odd or even
            # Odd Palindrome, one center character at index 'i'.
            substringi = findPalindromeSubstringFromCenter(i, i, s)
            if len(substringi) > len(longPal):
                longPal = substringi
            # Even Palindrome, two center characters at indices 'i' and 'i+1'.
            substringi = findPalindromeSubstringFromCenter(i, i+1, s)
            if len(substringi) > len(longPal):
                longPal = substringi
        return longPal
        
