'''
A signed, 32-bit integer x is given to have its digits reversed. 
This was done by repeatedly finding the remainder of x when divided 
by 10, giving the current last digit of x, and placing that as the
last digit of the reversed x. 
Each time this was done:
    x was updated to be divided by 10 to remove the last digit.
    The reversed x was multipled by 10 before each addition to 
    shift the previous addition forward.

Assumptions: 
-2^31 <= x <= 2^31 - 1
Environment doesn't allow 64-bit integers (signed or unsigned) to be stored.
'''

class Solution:
    def reverse(self, x: int) -> int:
        INT32_MAX = pow(2, 31) - 1
        INT32_MIN = -2 ** 31
        rev = 0
        xneg = x < 0
        if xneg:
            # Environment doesn't allow storage of 64-bit integers
            # If making x positive would result in such a situation, perform first calculation before changing x's sign.
            # Since the only value this would occur for will result in a 0 anyway, it is easier to go on and return 0.
            if x == pow(-2, 31): 
                return 0
        
        x = abs(x)

        # Continue this loop until the original value is empty.
        while x!=0: 
            # For each digit added, make sure that the reversed number isn't
            # outside of the range for a 32-bit integer.
            if(rev > INT32_MAX/10 or rev < INT32_MIN/10):
                return 0
            rev = rev * 10 + x%10
            x //= 10
        
        # Add a negative to the final value if the original was negative.
        return -1 * rev if xneg else rev
