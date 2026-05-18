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

        def iterative_search(a, b):

            while a <= b:
                mid = (a + b) // 2

                if array_to_scan[mid][0] == timestamp:
                    return array_to_scan[mid][1]
                
                if array_to_scan[mid][0] > timestamp:
                    b = mid - 1
                else:
                    a = mid + 1
            
            if b >= 0 and array_to_scan[b][0] < timestamp:
                return array_to_scan[b][1]
            else:
                return -1

        return iterative_search(0, len(array_to_scan) - 1)
                
        
