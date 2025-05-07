def solveNQueens(n: int):
    res = []
    board = [['.' for _ in range(n)] for _ in range(n)]

    def isSafe(row, col):
        # check in column
        for i in range(row):    
            if (board[i][col] == 'Q'):
                return False
            
        # check in positive diagonal
        i = row
        j = col
        while (i >= 0 and j < n):
            if (board[i][j] == 'Q'):
                return False
            i -= 1
            j += 1

        # check in negative diagonal
        i = row
        j = col
        while (i >= 0 and j >= 0):
            if (board[i][j] == 'Q'):
                return False
            i -= 1
            j -= 1

        return True

    def backtrack(row):
        if (row == n):
            res.append([''.join(row) for row in board])
            return False
        for col in range(n):
            if (isSafe(row, col)):
                board[row][col] = 'Q'
                possible = backtrack(row+1)
                if (possible):
                    return True
                board[row][col] = '.'
        return False
    
    backtrack(0)
    return res

def printSolutions(boards):
    for board in enumerate(boards):
        print(f"Solution {board[0]+1}")
        for row in board[1]:
            for col in row:
                print(col, end=' ')
            print()
        print()

if __name__ == "__main__":
    boards = solveNQueens(8)
    printSolutions(boards)

'''
 N-Queens Problem – Theory
🧠 Goal:
Place N queens on an N×N chessboard such that:

No two queens attack each other.

A queen can attack:

Horizontally

Vertically

Diagonally

 Approach: Backtracking
🌱 Basic Idea:
Start placing queens row by row.

For each row, try placing a queen in all columns.

Before placing, check if the position is safe.

If yes, move to the next row.

If placing a queen leads to no solution, backtrack and try the next column.

solveNQueens(board, row):
    if row == N:
        print/collect the board configuration
        return

    for col in 0 to N-1:
        if isSafe(board, row, col):
            place queen at (row, col)
            solveNQueens(board, row + 1)
            remove queen from (row, col)  // backtrack
🔎 isSafe(board, row, col):
Check:

Column: No queen in the same column above

Upper-left diagonal

Upper-right diagonal
Time Complexity: O(N!)
(Each queen can go to N columns in worst case, reducing choices row-wise)

Space Complexity: O(N²) for the board or O(N) for column/diagonal trackers

 Applications:
Constraint satisfaction problems

AI and game theory

Parallel task scheduling

Genetic algorithms (fitness functions)
'''