class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        res = 1
        sign = [None] * n

        for i in range(1, n):
            diff = arr[i] - arr[i - 1]
            if diff == 0:
                continue
            else:
                sign[i] = diff > 0

        l = 0
        for r in range(1, n):
            if sign[r] == None:
                l = r
            elif sign[r - 1] != None and sign[r - 1] == sign[r]:
                l = r - 1
            res = max(res, r - l + 1)

        return res
