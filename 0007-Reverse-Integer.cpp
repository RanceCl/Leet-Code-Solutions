/* 
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
*/

class Solution {
public:
    int reverse(int x) {
        int reversed_x = 0;
        
        // Continue this loop until the original value is empty.
        while(x){
            // For each digit added, make sure that the reversed number isn't 
            // outside of the range for a 32-bit integer
            if(reversed_x > INT_MAX/10 || reversed_x < INT_MIN/10) return 0;

            // Place the remainder of the current x value into the final digit of reversed_x
            reversed_x = reversed_x*10 + x%10;
            x = x/10;
        }
        return reversed_x;
    }
};
