from typing import List


def topKFrequent1(nums: List[int], k: int) -> List[int]:

    # THOUGHT PROCESS 
    # what i need to take given an array return the top k frequent elements 
    # in the example being the top 2 it would be 1 and 2 (occuring 3 and 2 times)
    # firstly create a hash map which will track the value and count for each number
    # cannot sort because solution has to be better than n log n
    # so i want to create a heap (array in python), 
    # Each index represents a frequency, storing values that occur that many times.
    # then iterate throuh that heap appending the results until the results is the same length as k
    counts = {} # val : frequency
    heap = [[] for _ in range(len(nums) + 1)]

    res = []

    for num in nums:
        counts[num] = 1 + counts.get(num, 0) 
    

    for num, count in counts.items(): 
        heap[count].append(num)
        

    for i in range(len(heap) - 1, 0, -1): 
        for n in heap[i]: 
            res.append(n)
            if len(res) == k: 
                return res

def topKFrequent2(nums: List[int], k: int) -> List[int]:
    res = []
    count = {}

    for num in nums: 
        count[num] = count.get(num, 0) + 1
    

    sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
    
    for item in sorted_items[:k]: 
        res.append(item[0])
    
    return res

nums = [1,1,1,2,2,3]
k = 2

nums2 = [1]
k2 = 1

nums3 = [1,2,1,2,1,2,3,1,3,2] 
k3 = 2

print(topKFrequent2(nums3, k3))