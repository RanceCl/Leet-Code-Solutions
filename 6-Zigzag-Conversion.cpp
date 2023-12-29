/*
A string, s, is to be given to be converted into a zigzag pattern, with the number
of rows for the zigzag being given as well. The string must be converted and then
read line by line into a single line string to be output.

I did this by creating a temporary vectory which would store the string in zigzag 
form. The row that a letter would be placed on would be determined by the row 
index, which would be increasing or decreasing depending on if the current point 
was moving up or down in the zigzag. 

For reference, for a zigzag with 5 rows, the direction for each letter would be
as follows. So the letter in the original string at index 3 would be moving down
while the letter at index 4 would be moving up (index starting at 0).

D     D     D
D   U D   U D
D  U  D  U  D
D U   D U   
U     U     

After the zigzag was completely stored, it would be read line by line and stored
in a single, one line string, which would be output.

If a zigzag of only one row was desired, it would simply be the original string.
*/

class Solution {
public:
    string convert(string s, int numRows) {
        if(numRows <= 1) return s;

        // Initialize the row index and direction value.
        int rowi = 0;
        bool movingUp = true;

        vector<string>temp(numRows, "");

        for (int i = 0; i < s.length(); i++){
            // Change direction of the zigzag if either boundary has been hit
            if ((rowi == 0) || (rowi == numRows-1)) movingUp = !movingUp;

            // Add the letter to the end of the appropriate row in the temporary string vector
            temp[rowi] += s[i];
            
            // Increment or decrement the row value depending on the current direction.
            if(movingUp) rowi--;
            else rowi++;
        }

        string zigzag;

        // Add together each row of the temporary vector into a single, one line string.
        for(int i = 0; i<numRows; i++) zigzag += temp[i];
        
        return zigzag;
    }
};
