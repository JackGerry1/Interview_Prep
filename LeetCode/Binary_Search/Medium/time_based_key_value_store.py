class TimeMap:

    def __init__(self):
        self.key_hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.key_hashmap: 
            self.key_hashmap[key] = []
        
        self.key_hashmap[key].append([value, timestamp]) 
    
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_hashmap: 
            return ""
        
        entries = self.key_hashmap[key]
        res = ""     
        l = 0 
        r = len(entries) - 1
        
        while l <= r: 
            mid = (l + r) // 2
            
            val, ts = entries[mid]
            
            if ts <= timestamp:
                res = val
                l = mid + 1
            else: 
                r = mid - 1
        
        return res 
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)