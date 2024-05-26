'''
A Roman numeral value was given to be converted into its corresponding integer variable. 
Proper formatting for numbers, like using IV instead of IIII for 4 was expected.

The general solution was to loop through the string, adding the corresponding number to
the final total for each character.

To account for the instances of subtraction in Roman numerals, the string would be read
backwards, with the number value of the previously read numeral being compared to the 
current one. If the previous numeral represented a larger value (such as in IV for 4),
then the current numeral's value would be subtracted, rather than added.

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
        prevVal = 0
        
        # Loop through the string backwards and add the appropriate number for each character.
        for c in s[::-1]:
            # If the previously read value wasn't larger than the current value, it should be added.
            if prevVal <= romanToIntDict[c]:
                numFinal += romanToIntDict[c]
            
            # If the previously read value was larger than the current one, it is a subtraction case
            # (I = 1, V = 5, IV = 4 = 5-1)
            else: 
                numFinal -= romanToIntDict[c]
            prevVal = romanToIntDict[c]
        return numFinal
