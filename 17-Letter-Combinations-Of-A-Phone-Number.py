'''
LeetCode Problem 17: Letter Combinations of a Phone Number

A string of digits ranging from 2-9 (inclusive) is given, with each number 
corresponding to digits on a phone keypad. Given this string of digits, a
list containing every possible letter combination for the numbers given was
requested. 

This was done by using a recursive method backtrack and explore every possible
combination before appending it to the list. 

Assumptions:
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        phoneKeys = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        # Recursive backtracking function to loop to the end of each possible combination and 
        # add each to the final list.
        def digitToKey(digitsRemain, strToAdd):
            #Check if the end of the number sequence has been reached
            if not digitsRemain:
                letterCombos.append(strToAdd)
            else:
                for letter in phoneKeys[digitsRemain[0]]:
                    # Add each letter to the end of the current string combination
                    digitToKey(digitsRemain[1:], strToAdd + letter)
        
        letterCombos = []
        digitToKey(digits, "")
        
        return letterCombos
