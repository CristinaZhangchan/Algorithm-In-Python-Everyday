class Solution:
    def solveSudoku(self, board):
        def isValid(board, row, col, c):
            for i in range(9):
                if board[row][i] == c: return False
                if board[i][col] == c: return False
                if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == c: 
                    return False
            return True

        def solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for c in map(str, range(1, 10)):
                            if isValid(board, i, j, c):
                                board[i][j] = c
                                if solve(board): return True
                                board[i][j] = '.'
                        return False
            return True

        solve(board)

board =board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
solution = Solution()
solution.solveSudoku(board)

print("\nSolved Board:")
for r in range(len(board)):
    # Every 3 rows, print a separator line for readability
    if r % 3 == 0 and r != 0:
        print("-" * 21)
    
    # Format the row with "|" separators for 3x3 blocks
    formatted_row = ""
    for c in range(len(board[r])):
        if c % 3 == 0 and c != 0:
            formatted_row += "| "
        formatted_row += board[r][c] + " "
    
    print(formatted_row)