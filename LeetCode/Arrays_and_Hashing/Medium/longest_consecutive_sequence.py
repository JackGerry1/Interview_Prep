from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_seq = 0 
        
        for n in num_set: 
            if (n - 1) not in num_set:
                current_streak = 1
                while (n + current_streak) in num_set: 
                    current_streak += 1 
                longest_seq = max(current_streak, longest_seq)
        
        return longest_seq