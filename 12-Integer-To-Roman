'''
An integer was given to be converted into its corresponding Roman numeral variable. 
Proper formatting for numbers, like using IV instead of IIII for 4 was expected.

To do this, I simply placed all of the Roman numeral numbers into a dictionary, looping
through the number and dividing it by the largest value possible, updating it with each
calculation until every value in the dictionary was checked. The number of times that the
input could be divided by the current number value would be the amount of times its 
corresponding Roman Numeral would be added to the final string.

Assumptions:
1 <= num <= 3999
'''

class Solution:
    def intToRoman(self, num: int) -> str:
        intToRomanDict = {
            1000: "M", 900: "CM",
            500: "D", 400: "CD", 
            100: "C", 90: "XC",
            50: "L", 40: "XL",
            10: "X", 9: "IX",
            5: "V", 4: "IV",
            1: "I"
        }
        
        romanFinal = ""
        # Divide by each letter to get what they all are. 
        for intVal, romVal in intToRomanDict.items():
            # Find the number of times each roman numeral should repeat. 
            romanFinal += (romVal * (num//intVal))
            # Update number.
            num = num % intVal
        
        return romanFinal
