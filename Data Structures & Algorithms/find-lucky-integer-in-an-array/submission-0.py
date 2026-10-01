class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        res = -1

        for num, count in counter.items():
            if num == count:
                res = max(res, num)

        return res
