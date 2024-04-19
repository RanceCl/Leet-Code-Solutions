'''
A Roman numeral value was given to be converted into its corresponding integer variable. 
Proper formatting for numbers, like using IV instead of IIII for 4 was expected.

The general solution was to loop through the string, adding the corresponding number to
the final total for each character.

To account for the instances of subtraction in Roman numerals, a simple solution was found
by replacing every numeral combination that would require subtraction with a form that was
easier to read. IV would be replaced with IIII, IX with VIIII, XL with XXXX, and so on. Then
the string could be looped through in its entirety with no issue. 

Assumptions:
1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        romanToIntDict = {
            "I": 1,
            "V": 5, 
            "X": 10, 
            "L": 50, 
            "C": 100, 
            "D": 500, 
            "M": 1000
        }
        
        numFinal = 0

        # Convert subtraction rule numerals into an easier to read format.
        s = s.replace("IV", "IIII")
        s = s.replace("IX", "VIIII")
        s = s.replace("XL", "XXXX")
        s = s.replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC")
        s = s.replace("CM", "DCCCC")

        # Loop through the string and add the appropriate number for each character.
        for c in s:
            numFinal += romanToIntDict[c]
        
        return numFinal
