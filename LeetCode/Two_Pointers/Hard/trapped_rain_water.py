from typing import List


class Solution: # O(n) space
    def trap(self, height: List[int]) -> int:
        if not height: 
            return 0
        
        trapped_water = 0

        left_max = [0] * len(height)
        right_max = [0] * len(height)

        for i in range(1, len(height)):
            left_max[i] = (max(left_max[i - 1], height[i - 1]))

        for i in range(len(height) - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i + 1])

        for i in range(len(height)): 
            water = min(left_max[i], right_max[i]) - height[i]

            if water > 0: 
                trapped_water += water

        return trapped_water
    
    def trap(self, height: List[int]) -> int: # O(1) space
            if not height: 
                return 0
        
            l = 0 
            r = len(height) - 1
            trapped_water = 0
            maxleft = height[l]
            maxright = height[r]

            while l < r: 
                if maxleft < maxright: 
                    l += 1
                    maxleft = max(maxleft, height[l])
                    trapped_water += maxleft - height[l]
                else: 
                    r -= 1
                    maxright = max(maxright, height[r])
                    trapped_water += maxright - height[r]

            return trapped_water