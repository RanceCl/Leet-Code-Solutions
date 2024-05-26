'''
Given two integers dividend and divisor, divide two integers without 
using multiplication, division, and mod operator. The integer 
division should truncate toward zero, which means losing its 
fractional part.

Return the quotient after dividing dividend by divisor.

This was done using bit manipulation and subtraction.

For bit manipulation, we would double the divisor by the dividend 
until it couldn't fit anymore, subtracting this and storing the
multiple that could be taken.

We would start with the bit count of the largest possible multiple of
the divisor that could fit in the dividend, n. Then we could go 
through a loop until the last bit is reached, n = 0. For each count, 
we would check if shifting the divisor by n bits would result in a 
number that could be taken from the dividend. If so, subtract this 
number and increase the quotient by 2^n, or 1 shifted forward by n 
bits. At the end, the result would be made negative if the result 
should be. 

Assumptions:
-2^31 <= dividend, divisor <= 2^31 - 1
divisor != 0
'''
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT32_MAX = 2147483647
        INT32_MIN = -2147483648
        
        # Our single overflow case
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        # Determine the sign of the quotient and make any negative integer positive
        negQuotient = False
        if dividend<0:
            negQuotient = not negQuotient
            dividend = ~dividend + 1
        if divisor<0:
            negQuotient = not negQuotient
            divisor = ~divisor + 1
        
        # Find the largest multiple of the divisor that is less than or equal to the dividend
        bitCount = 0
        while dividend >= (divisor << (1+bitCount)):
            bitCount += 1
            
        quotient = 0
        # Start from the largest multiple of the divisor that can fit and work down
        for i in range(bitCount,-1,-1):
            # Make sure that the multiplied divisor fits into the dividend (divisor * 2 * i)
            if (divisor << i) <= dividend:
                dividend -= divisor << i
                quotient += 1 << i
        # Make the result negative if the sign of the inputs would result in a negative answer
        return (~quotient + 1) if negQuotient else quotient
