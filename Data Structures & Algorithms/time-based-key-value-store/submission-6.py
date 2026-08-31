class TimeMap:

    def __init__(self):
        self.hash_map={}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash_map:
            self.hash_map[key]=[]
        self.hash_map[key].append([value,timestamp])
    
    def get(self, key: str, timestamp: int) -> str:
        res=""
        vals = self.hash_map.get(key,[])
        l,r=0,len(vals)-1
        while l<=r:
            m=l+((r-l)//2)
            if vals[m][1]<=timestamp:
                res=vals[m][0]
                l=m+1
            else:
                r=m-1
        return res
        