import math
from typing import List, Self


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 
        r = max(piles)
        res = 0

        while l <= r: 
            speed = (l + r) // 2

            total_time = 0
            for pile in piles: 
                total_time += math.ceil(pile / speed)

            print(f"speed: {speed}")
            print(f"totaltime: {total_time}")

            if total_time > h: 
                l = speed + 1
            elif total_time <= h: 
                res = speed
                r = speed - 1
        return res

print(Solution.minEatingSpeed(Self, piles=[30,11,23,4,20], h=5))