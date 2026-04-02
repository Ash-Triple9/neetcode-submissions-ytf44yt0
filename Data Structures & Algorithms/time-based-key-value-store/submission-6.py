class TimeMap:

    def __init__(self):
        self.timeMap = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.timeMap:
            self.timeMap[key] = [[value, timestamp]]
        else:
            self.timeMap[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:   
        if not key in self.timeMap:
            return ""
        l = 0
        r = len(self.timeMap[key])-1
        m = 0

        while l<r:
            m = (l+r)//2
            mapStamp = self.timeMap[key][m][1]
            mapValue = self.timeMap[key][m][0]
            if mapStamp == timestamp:
                return mapValue
            elif timestamp > mapStamp:
                l = m+1
            elif timestamp < mapStamp:
                r = m-1
        if self.timeMap[key][l][1] <= timestamp:
            print(self.timeMap[key][l][0])
            return self.timeMap[key][l][0]
        elif self.timeMap[key][m][1] <= timestamp:
            print(self.timeMap[key][m][0])
            return self.timeMap[key][m][0]
        else: return ""
        
