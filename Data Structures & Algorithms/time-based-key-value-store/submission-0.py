class TimeMap:
    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.map[key]

        if not values:
            return ""

        l, r = 0, len(values) - 1

        while l < r:
            mid = (l + r) // 2

            if values[mid][0] > timestamp:
                r = mid
            else:
                l = mid + 1

        if values[l][0] > timestamp:
            return values[l - 1][1] if l - 1 >= 0 else ""

        return values[l][1]
