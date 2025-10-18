from typing import List

def maxArea(height: List[int]) -> int:
    l = 0 
    r = len(height) - 1
    max_area = 0        
    while l < r:
        width = r - l
        if height[l] <= height[r]:
            temp_max_area = height[l] * width
            l += 1

        else: 
            temp_max_area = height[r] * width
            r -= 1

        max_area = max(temp_max_area, max_area)


    return max_area

height1 = [1,7,2,5,4,7,3,6]
height2 = [1,8,6,2,5,4,8,3,7]

print(maxArea(height1))
print(maxArea(height2))

