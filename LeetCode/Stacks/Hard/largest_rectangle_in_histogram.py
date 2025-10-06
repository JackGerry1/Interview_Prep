from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        height_max = 0 
        stack = []
        # padding zero so if the standard input never gets into the while loop eg [2, 4] we append a 0 
        # so it becomes [2, 4, 0] so on the last iteration it pops the last element it last element calculates the width in this case 4 * 1 = 4
        # still in while loop because zero is the smallest value the stack is now empty with value 2 so we 2 * i which is 2 so 2 * 2 = 4 
        # now there is no stack so we append zero to the stack and no heights so we return height_max 
        heights.append(0)

        for i, h in enumerate(heights): 
            while stack and h < heights[stack[-1]]: 
                idx = stack.pop()
                height = heights[idx]
                width = i if not stack else i - stack[-1] - 1
                height_max = max(height_max, height * width)
        
            stack.append(i)
        
        
        return height_max
    
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_height = 0 
        stack = []
    
        for i, h in enumerate(heights):
            start = i
            
            # if the answer does not cover the entire area of the bar chart 
            # eg 1, 1, 1 = max area is 1 * len(heights) = 3 * 1 = 3 
            while stack and stack[-1][1] > h: 
                index, height = stack.pop()
                max_height = max(max_height, height * (i - index))
                start = index
            stack.append([start, h])
        
        # if the answer is the area from the start to finish
        for i, h in stack: 
            max_height = max(max_height, h * (len(heights) - i))
            
        return max_height