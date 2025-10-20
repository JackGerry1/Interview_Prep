from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        l = 0 
        r = (ROWS * COLS) - 1
        
        while l <= r: 
            midpoint = (l + r) // 2
            
            rows = midpoint // COLS
            cols = midpoint % COLS
            
            if matrix[rows][cols] < target: 
                l = midpoint + 1
            
            elif matrix[rows][cols] > target: 
                r = midpoint - 1
            
            else: 
                return True
        
        return False