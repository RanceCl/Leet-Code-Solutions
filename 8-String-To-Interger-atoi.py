'''
A string, s, is given to be converted into a 32-bit signed integer using the given myAtoi algorithm: 
1.  Read in and ignore any leading whitespace.
2.  Check if the next character (if not already at the end of the string) is '-' or '+'. Read 
    this character in if it is either. This determines if the final result is negative or positive 
    respectively. Assume the result is positive if neither is present.
3.  Read in next the characters until the next non-digit character or the end of the input is reached. 
    The rest of the string is ignored.
4.  Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then 
    the integer is 0. Change the sign as necessary (from step 2).
5.  If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so 
    that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and 
    integers greater than 231 - 1 should be clamped to 231 - 1.
6.  Return the integer as the final result.

Assumptions: 
0 <= s.length <= 200
s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
'''
class Solution:
    def myAtoi(self, s: str) -> int:
        INT32_MIN,INT32_MAX = -(2 ** 31), pow(2, 31) - 1

        # Remove the leading whitespace.
        s = s.lstrip(' ')

        # Make sure the resulting string isn't empty.
        if len(s) == 0:
            return 0

        # Check for '-' or '+'
        sign, digitCounter = self.findSign(s)
        if digitCounter != 0:
            s = s[1:]

        result = sign * self.convertStringToInt(s)
        
        # Clamp the final value
        result = self.clampValue(result,INT32_MIN,INT32_MAX)
        return result

    # Check for '-' or '+' and give the result the proper sign.
    def findSign(self, s):
        if s[0] == '-': return -1, 1
        elif s[0] == '+': return 1, 1
        return 1, 0

    # Clamps the value, x, between the minimum and maximum values sent.
    def clampValue(self, x, minVal, maxVal):
        if x < minVal: return minVal
        elif x > maxVal: return maxVal
        return x
    
    # Converts every character to an integer until the first non-numeric value.
    def convertStringToInt(self, s):
        result = 0
        charToIntDict = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        for i in s:
            if i in charToIntDict: result = (result * 10) + charToIntDict[i]
            else: break
        return result
