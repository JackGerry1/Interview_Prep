from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        s1_dict = Counter(s1)
        s2_dict = Counter(s2[:s1_len])
        
        if s1_len > s2_len: 
            return False
        
        if s1_dict == s2_dict: 
            return True 
        
        
        for r in range(s1_len, s2_len):
            new_char = s2[r]
            s2_dict[new_char] += 1
    
            old_char = s2[r - s1_len]
            s2_dict[old_char] -= 1
            
            if s2_dict[old_char] == 0:
                del s2_dict[old_char]
                
            if s1_dict == s2_dict: 
                return True 
        
        return False