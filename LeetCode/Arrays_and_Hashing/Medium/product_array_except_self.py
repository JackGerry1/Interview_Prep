from typing import List


def productExceptSelf(nums: List[int]) -> List[int]: # O(n) time | O(1) space
        output = [1] * len(nums)
        prefix = 1 
        postfix = 1

        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        for j in range(len(nums) - 1, -1, -1):
            output[j] *= postfix
            postfix *= nums[j]

        return output 
def productExceptSelf(nums: List[int]) -> List[int]: # O(n) time | O(n) space
    left_arr = [0] * len(nums)
    right_arr = [0] * len(nums)
    
    left_mult = 1 
    right_mult = 1 
    
    for i in range(len(nums)): 
        left_arr[i] = left_mult
        left_mult *= nums[i]
    
    for j in range(len(nums) - 1, -1, -1):
        right_arr[j] = right_mult
        right_mult *= nums[j]

    
    res = [l * r for l, r in zip(left_arr, right_arr)]

    return res