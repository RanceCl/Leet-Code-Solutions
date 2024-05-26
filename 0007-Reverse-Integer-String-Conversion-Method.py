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

        xstr = str(abs(x))
        if(len(xstr) < 10):
            rev = int(xstr[::-1])
        # In order to prevent the final result from being outside of the range for a signed 32-bit integer, 
        # the reversal calculations will be split into two parts.
        else:
            rev = int(xstr[1:][::-1])
            lastdigit = int(xstr[0])

            # Combine the two slices together if the result won't be outside of the signed 32-bit integer range.
            if(rev > INT32_MAX/10 or rev < INT32_MIN/10):
                return 0
            else:
                rev = (rev * 10) + lastdigit

        # Add a negative to the final value if the original was negative.
        return -1 * rev if x<0 else rev
