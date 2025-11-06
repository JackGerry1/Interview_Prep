from typing import List

def lengthOfLongestSubstring(s: str) -> int:
    charSet = set()
    l, r = 0, 0
    res = 0 
    
    for r in range(len(s)): 
        while s[r] in charSet: 
            charSet.remove(s[l])
            l += 1
        
        charSet.add(s[r])
        res = max(res, len(charSet))
        
    return res 
    


s = "zxyzxyz"
s2 = "xxxx"

print(lengthOfLongestSubstring(s))
print(lengthOfLongestSubstring(s2))