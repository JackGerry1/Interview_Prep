from typing import List
from collections import defaultdict

def isValidSudoku(board: List[List[str]]) -> bool:
    rows = defaultdict(set)
    cols = defaultdict(set)
    three_grid = defaultdict(set)
    
    for r in range(len(board)):
        for c in range(len(board[r])): 
            if board[r][c] == ".": 
                continue
            if board[r][c] in rows[r]: 
                return False
            if board[r][c] in cols[c]: 
                return False
            if board[r][c] in three_grid[(r, c)]: 
                return False

            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            three_grid[(r // 3, c // 3)].add(board[r][c])

    return True


board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))