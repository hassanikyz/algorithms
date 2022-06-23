 def solveNQueens( n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        col = set()
        posDiag = set()
        negDiag = set()
        
        res = []
        board = [["."] * n for i in range(n)]

        
        def backtrack(r):
            
            if r == n:
                copy = [ "".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                    
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r -c)
                board[r][c] = 'Q'
                
                backtrack(r+1)
               
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r -c)
                board[r][c] = '.'
                
        backtrack(0)
        return res
                
                
                    
                
#         def validate(board, n):
        
#             #check every row for collision
#             for row in board:
#                 if row.sum() > 1:
#                     return False

#             #check columns for collision
#             columns = board.shape[1]
#             for col in range(columns):
#                 if board[:, col].sum() > 1:
#                     return False
#             #check diagonal for collision
#             # 
#             for x in range(0, n):
#                 l = np.diag(board, k=x)

#                 if l.sum() > 1:
#                     return False

#             for x in range(0, n):
#                 l = np.diag(board, k=-x)
 
#                 if l.sum() > 1:
#                     return False

#             mirror_board = np.fliplr(board)
#             for y in range(0, n):
#                 l = np.diag(mirror_board, k=y)
#                 if l.sum() > 1:
#                     return False

#             for y in range(0, n):
#                 l = np.diag(mirror_board, k=-y)
#                 if l.sum() > 1:
#                         return False

#             return True
        

#         def solve(board, col, n, startRow):

#             # if board is solved return True
            
#             if validate(board, n):
#                 if board.sum() == n:
#                     tempBoard = board.copy()
#                     tempBoard = tempBoard.astype(str)
#                     tempBoard[tempBoard == '1'] = 'Q'
#                     tempBoard[tempBoard == '0'] = '.'
#                     result = []
#                     for r in tempBoard:
#                         s = ''.join(r)
#                         result.append(s)
#                     allboards.append(result)
#                     #return True
#                     if col == len(board[0]) and board[:,0][n-1] == 1:
#                         return True
#                     else:
#                         col = 0
#                         for i in range(0, n):
#                             if board[:,0][i] == 1:
#                                 startRow = i+1
#                                 if startRow >= len(board[:,0]) - 1:
#                                     return True
#                         board[board == 1] = 0
#                         solve(board, 0, n, startRow)
#                         return True
                        

#                 for row in range (startRow,n):
#                     board[row, col] = 1
#                     if validate(board, n):
#                         if solve(board, col+1, n, 0):
#                             return True
#                         board[row,col] = 0
#                     else:
#                         board[row,col] = 0

#             return False
        
#         startRow = 0
#         allboards = []
#         board = np.zeros((n, n))
#         board = board.astype(int)
#         # print(board)
#         solve(board, 0, n, startRow)
#         # board = board.astype(str)
#         # board[board == '1'] = 'Q'
#         # board[board == '0'] = '.'
#         # print(board)
#         # print(allboards)
#         return allboards
