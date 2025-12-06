from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        dq = deque()
        l = 0 
        r = 0 

        while r < len(nums):

            # if the queue is not empty 
            # and the current value of nums is greater than the most recent element in the queue 
            # pop it because we want to keep a queue in decreasing order (4, 3, 2) == valid (4, 3, 5) invalid
            # after doing this while loop appened the nums[r] 
            while dq and nums[r] > nums[dq[-1]]: 
                dq.pop()
            dq.append(r)

            window_size = r - l 
            start_of_window = r - k + 1

            # if value of index in queue less than start index of window
            # the window has moved to the right therefore this element is not needed and can be popped. 
            if dq[0] < start_of_window: 
                dq.popleft()

            # if the window size == the size of k (size of sliding window) append value by getting index 
            # from the queue 
            if window_size == k - 1: 
                output.append(nums[dq[0]])
                l += 1

            r += 1


        return output