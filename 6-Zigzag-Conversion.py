'''
A string, s, is to be given to be converted into a zigzag pattern, with the number
of rows for the zigzag being given as well. The string must be converted and then
read line by line into a single line string to be output.

I did this by creating a temporary vector which would store the string in zigzag 
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
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s

        # Initialize the row index and the direction value
        rowi = 0
        movingUp = True
        temp = [""] * numRows

        # Loop
        for schar in s:
            # Change direction of the zigzag if either boundary has been hit
            if ((rowi == 0) or (rowi == numRows-1)):
                movingUp = not movingUp

            temp[rowi] += schar

            # Increment or decrement the row value depending on the current direction.
            if movingUp:
                rowi -=1
            else:
                rowi +=1
        
        return "".join(temp)

