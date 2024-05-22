'''
Given two strings needle and haystack, return the index of the first 
occurrence of needle in haystack, or -1 if needle is not part of 
haystack.

This was done using a sort of sliding window of needle's length, 
comparing this substring of haystack to needle until either a match 
was found or the loop had reached its end.

Since needle can only be found if the number of remaining characters 
is greater than or equal to needle's, the loop only needs to continue
until haystack's is less than needle's.

Assumptions:
1 <= haystack.length, needle.length <= 10^4
haystack and needle consist of only lowercase English characters.
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            # Shifting window of needle's length
            if haystack[i:i+len(needle)] == needle: 
                return i
        return -1
