def twoSum(nums: List[int], target: int) -> List[int]:
    
    val_index_map = {}
    for i, n in enumerate(nums): 
        diff = target - n 
        if diff in val_index_map: 
            return [val_index_map[diff], i]
        val_index_map[n] = i
        