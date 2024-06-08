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
For every row or column, we can add every value in each to a set. Duplicate 
values won't be added again. 
    If the number of elements in the set isn't the same as the number of 
    elements in its corresponding row or column, then that means that said 
    row or column contains a duplicate and the matrix is invalid. 

    If the end of the for loops to check this are reached without issue, 
    then no rows or columns had duplicates, and therefore are valid.

Since the number of rows and columns in the matrix are the same, we can 
perform this check on both at the same time, rather than requiring two 
separate sets of nested for loops to check each.

Assumptions: 
n == matrix.length == matrix[i].length
1 <= n <= 100
1 <= matrix[i][j] <= n
'''
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        # Since len(row) == len(col), can check both at once
        for i in range(n): 
            # Reset each set at beginning of new row/col
            rowCheck = set()
            colCheck = set()
            for j in range(n): 
                # Add value at each index to set. Repeats won't be added
                colCheck.add(matrix[i][j])
                rowCheck.add(matrix[j][i])
                # If repeats, all numbers can't be in row/col
                if (len(rowCheck) != j+1) or (len(colCheck) != j+1):
                    return False
        return True
