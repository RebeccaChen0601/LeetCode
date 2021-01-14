#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']*n for _ in range(n)]
        res = []
        def isValid(row, col, board):
            for r in range(row):
                if board[r][col] == 'Q':
                    return False
                if  col-row+r >= 0 and board[r][col-row+r] == 'Q':
                    return False
                if col+row-r < n and board[r][col+row-r] == 'Q':
                    return False 
            return True

        def dfs(row):   
            if row == n:
                temp = []
                for row in range(n):
                    temp.append(''.join(list(board[row])))
                res.append(temp) 
                return
            
            for col_i in range(len(board)):
                board[row][col_i] = 'Q'
                if isValid(row, col_i, board):
                    dfs(row+1)
                board[row][col_i] = '.'
            
        dfs(0)
        return res
# @lc code=end

