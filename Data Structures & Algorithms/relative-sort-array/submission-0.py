class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        pos = {n: i for i, n in enumerate(arr2)}
        arr1.sort(key=lambda x: pos[x] if x in pos else x + 1000)
        return arr1
