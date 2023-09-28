class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        
        res = ""
        values = self.hashmap.get(key, [])

        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            # if the mid is equal or lower than timestamp, then update result and move l pointer to right
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                # if the mid is too high, then r pointer needs to shift down.
                r = m - 1
    
        return res