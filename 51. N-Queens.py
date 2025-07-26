





























































ee
eeeeeff

class Solution:
    def solveNQueens(self, n):



        
        def backtrack(row):
            if row == n:
                board = [''.join('Q' if i == col else '.' for i in range(n)) for col in queens]
                solutions.append(board)
                return
            for col in range(n):
                if col in cols or (row + col) in diag1 or (row - col) in diag2:
                    continue
                queens[row] = col
                cols.add(col)
                diag1.add(row + col)
                diag2.add(row - col)
                backtrack(row + 1)
                cols.remove(col)
                diag1.remove(row + col)
                diag2.remove(row - col)

        solutions = []
        queens = [-1] * n
        cols = set()
        diag1 = set()
        diag2 = set()
        backtrack(0)
        return solutions



















