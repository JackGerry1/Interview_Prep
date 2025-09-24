
# Time Complexity = O(n) Space Complexity O(1)
def isAnagramV2(s: str, t: str) -> bool:
        freq_hashmap1 = {}
        freq_hashmap2 = {}
        
        if len(s) != len(t): 
            return False

        for char in s: 
            if char in freq_hashmap1: 
                freq_hashmap1[char] += 1
            else: 
                freq_hashmap1[char] = 1  
        
        for char in t: 
            if char in freq_hashmap2: 
                freq_hashmap2[char] += 1
            else: 
                freq_hashmap2[char] = 1 

        return freq_hashmap1 == freq_hashmap2

# Time Complexity = O(n log n) Space Complexity O(1) / O(n) depending on sorting algorthims
def isAnagramV1(s: str, t: str) -> bool: 
    return sorted(s) == sorted(t) 

