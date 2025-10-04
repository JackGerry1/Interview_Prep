from typing import List

# On^2
def dailyTemperatures(temperatures: List[int]) -> List[int]:
    res = []
        
    for i in range(len(temperatures)):
        found = False
        for j in range(i + 1, len(temperatures)):
            if temperatures[j] > temperatures[i]: 
                days = j - i
                found = True
                res.append(days)
                break
        if not found: 
            res.append(0)
    
    return res

# O(n)
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        mono_stack = [] # index, temp
        for idx, temp in enumerate(temperatures): 
            while mono_stack and temp > mono_stack[-1][1]: 
                stackidx, _ = mono_stack.pop()
                days = idx - stackidx
                res[stackidx] = days
            
            mono_stack.append([idx, temp])
        
        return res

temperatures = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(temperatures))