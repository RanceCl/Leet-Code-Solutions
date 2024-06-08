'''
An n x n matrix is valid if every row and every column contains all the 
integers from 1 to n (inclusive).

Given an n x n integer matrix matrix, return true if the matrix is valid. 
Otherwise, return false.

Since the numbers of the matrix can only be between 1 and n, that means 
that the only time where a row or column won't have every number is when 
there is a duplicate value in the row or column. 

Therefore, the problem can simply become a check to see if there are any 
duplicates. 

The can be very easily done with the help of sets since sets can't store 
duplicate values. 
For every row or column, we can simply place these values in a set. 
Duplicate values won't be added multiple times. Using zip, we can isolate 
each take the row or column as a whole and convert it to a set, checking 
to see if the number of unique elements in each set is equal to the length 
of the matrix.
    If the number of elements in the set isn't the same as the number of 
    elements in its corresponding row or column, then that means that said 
    row or column contains a duplicate and the matrix is invalid. 

    If the end of the for loops to check this are reached without issue, 
    then no rows or columns had duplicates, and therefore are valid.

Since the number of rows and columns in the matrix are the same, we can 
perform this check on both at the same time, rather than requiring two 
separate for loops to check each.

Assumptions: 
n == matrix.length == matrix[i].length
1 <= n <= 100
1 <= matrix[i][j] <= n
'''
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        
        # Make sure that no duplicates are found in each row and column
        # Zip helps isolate a single row and column each loop.
        # Since len(row) == len(col), we can check both at once
        for row, col in zip(matrix, zip(*matrix)): 
            # A duplicate is found if the set lengths aren't equal to n
            if len(set(row)) != n or len(set(col)) != n:
                # If a duplicate is detected, matrix can't be valid.
                return False
        # Matrix is valid if the end has been reached.
        return True
