class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.datas = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.datas:
            self.datas[key] = []
        self.datas[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.datas:
            return ''
        if self.datas[key][0][1]>timestamp:
            return ''
        values = self.datas[key]
        for i in range(len(values)-1, -1, -1):
            value, prev = values[i]
            if prev<=timestamp:
                return value
