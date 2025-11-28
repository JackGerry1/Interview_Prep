# my attempt 
from collections import Counter

def minWindow(s: str, t: str) -> str:
    t_len = len(t)
    s_len = len(s)    
    res = []
    is_subset = False
    if s_len < t_len: 
        return ""
    
    t_dict = Counter(t)
    s_dict = Counter(s[:t_len])
    
    
    for r in range(t_len, s_len): 
        is_subset = t_dict.keys() <= s_dict.keys()
        print(is_subset)
        
        while not is_subset: 
            s_dict[s[r]] += 1
            
        
        while is_subset:
            current_res = "".join(s_dict)
            res.append(current_res)
            
            s_dict[s[r - len(s_dict)]] -= 1
            
            if s_dict[s[r - len(s_dict)]] == 0: 
                del s_dict[s[r - len(s_dict)]]
            
        return min(res)
            
    
    
    return ""


s = "ADOBECODEBANC"
t = "ABC"

print(minWindow(s, t))


# working 
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        t_dict = Counter(t)
        s_dict = Counter()

        have = 0  
        need = len(t_dict)  
        res_range = [0, 0]  
        res_len = float("infinity")  

        l = 0

        for r in range(len(s)):  
            char = s[r]
            s_dict[char] += 1

            if char in t_dict and s_dict[char] == t_dict[char]:
                have += 1

            while have == need:
                window_size = r - l + 1

                if window_size < res_len:
                    res_len = window_size
                    res_range = [l, r]
                old_char = s[l]

                s_dict[old_char] -= 1
                if s[l] in t_dict and s_dict[s[l]] < t_dict[s[l]]:
                    have -= 1
                l += 1


        return s[res_range[0]:res_range[1] + 1] if res_len != float("infinity") else ""