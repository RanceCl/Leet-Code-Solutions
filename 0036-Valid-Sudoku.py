'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to 
be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 
without repetition.

Note:
    A Sudoku board (partially filled) could be valid but is not 
    necessarily solvable.
    Only the filled cells need to be validated according to the 
    mentioned rules.

The entire board was scanned through, with each value in the 2D array being 
stored with the index corresponding to whatever it would need be compared 
against.
    The row check, with each value and its corresponding row index.
    The column check, with each value and its corresponding column index.
    The sub-box check, with each value and what sub-box it is in.

Initially, I planned on having the three checks being done per iteration of 
the second for loop, similar to the set check implementation of problem 
2133. However, due to how this implementation would require three different 
checks for a "." per iteration, I deemed this to be more inefficient over 
all. 

Once every value is stored, the length of each would be compared with the 
length of what they would be as sets. Any repeat values for a the index of 
a row, column, or sub-box, would be removed, with a different length 
indicating that a repeat had been found. 

Assumptions:
    board.length == 9
    board[i].length == 9
    board[i][j] is a digit 1-9 or '.'.
'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Since len(row) == len(col) == 9, can check both at once
        rowCheck = []
        colCheck = []
        subBoxCheck = []
        for r in range(9):
            for c in range(9):
                cellVal = board[r][c]
                if cellVal != '.':
                    rowCheck += [(r, cellVal)]
                    colCheck += [(c, cellVal)]
                    subBoxCheck += [(r // 3, c // 3, cellVal)]
        return (
            len(rowCheck) == len(set(rowCheck)) and
            len(colCheck) == len(set(colCheck)) and
            len(subBoxCheck) == len(set(subBoxCheck))
            )
