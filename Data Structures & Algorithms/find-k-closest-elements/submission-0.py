class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        distance = 0
        res_start, res_end = 0, k

        for i in range(k):
            distance += abs(x - arr[i])

        min_distance = distance
        for i in range(n - k + 1):
            if distance < min_distance:
                res_start = i
                res_end = i + k
                min_distance = distance
            if i < n - k:
                distance = distance - abs(x - arr[i]) + abs(x - arr[i + k])
        
        return arr[res_start : res_end]
            