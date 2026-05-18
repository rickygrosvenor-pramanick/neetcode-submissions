class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = [(timestamp, value)]
        else:
            self.map[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
            
        array_to_scan = self.map[key]

        def search(a, b):

            if a >= b:
                return array_to_scan[b][1]
            
            mid = (a + b) // 2

            if array_to_scan[mid][0] == timestamp:
                return array_to_scan[mid][1]
            
            if array_to_scan[mid][0] > timestamp:
                return search(a, mid - 1)
            else:
                return search(mid + 1, b)
        
        value = search(0, len(array_to_scan) - 1)

        return value
                
        
